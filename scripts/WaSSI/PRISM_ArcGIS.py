import arcpy
import arcpy.sa as sa
import pandas as pd
import numpy as np
import numpy.ma as ma
import WaSSI_ArcGIS as WaSSI

import tools

# Set current workspace folder
arcpy.env.workspace = "C:/Users/DBP/Documents/ArcGIS"
prism_path = "E:/PRISM/"

# Enable spatial analysis toolkit
arcpy.CheckOutExtension("Spatial")

# Import the shapefile which defines the boundary of LA
la_shapefile_path = "C:/Users/DBP/Documents/ArcGIS/APC/APC.shp"
la_shapefile = arcpy.mapping.Layer(la_shapefile_path)

# Get the bounds from the shapefile. These set the rectangular bounding box only.
bounds = "-118.669433275236 33.7021128831574 -118.154627646908 34.3382533582622"

# Value that PRISM uses for NaN or No Data
PRISM_NaN = -9999

# Iterate over every month in years 1990-2015
years = range(1990, 2016)
months = ["01", "02", "03", "04", "05",
		  "06", "07", "08", "09", "10", "11", "12"]

# Create data frame for storing values
df_NaN = -1.0
parameters = ["PRCP", "ET", "AET"]
date_range = pd.date_range(start='1/1/1990', end='12/31/2015', freq='MS')
empty_array = np.array([df_NaN] * len(date_range) * len(parameters)
					   ).reshape((len(date_range), len(parameters)))
df = pd.DataFrame(empty_array, index=date_range,
				  columns=parameters, dtype=float)

# Import land use map & clip to bounds
landuse_bounds = "-2066855.180218 1418311.723318 -2004357.620718 1498465.598953"
landuse_NaN = 255
landuse_path = r"E:\nlcd_2001_landcover_2011_edition_2014_10_10\nlcd_2001_landcover_2011_edition_2014_10_10.img"
landuse_temp_raster = arcpy.Raster(landuse_path)

arcpy.Clip_management(landuse_temp_raster, landuse_bounds, "landuse", la_shapefile, landuse_NaN, "ClippingGeometry", "MAINTAIN_EXTENT")
landuse_raster = arcpy.Raster("landuse")
				  
for year in years:
	for month in months:
		# Load the precipitation raster
		raster_name = "PRISM_ppt_stable_4kmM3_{0}{1}_bil".format(year, month)
		raster_path = "{0}{1}/{1}.bil".format(prism_path, raster_name)
		raster = arcpy.Raster(raster_path)

		# Clip the PRISM raster to the LA shapefile's path, store the result in "raster_name" object
		# "ClippingExtent" clips the raster to a non-convex shape, allowing for more precision (i.e. not a square)
		# "NO_MAINTAIN_EXTENT" sets it to maintain the extents of the raster, not the shapefile (keep the lat/long coords for bounds)
		arcpy.Clip_management(raster, bounds, 'ppt_{}{}'.format(
			year, month), la_shapefile, PRISM_NaN, "ClippingGeometry", "MAINTAIN_EXTENT")
		raster = arcpy.Raster("ppt_{}{}".format(year, month))

		# Get the raster properties
		ncol = int(raster.width)  # No. of columns
		nrow = int(raster.height)  # No. of rows
		xmin = raster.extent.XMin  # Minimum X value
		xmax = raster.extent.XMax  # Maximum X value
		xdiff = float(arcpy.GetRasterProperties_management(
			raster, "CELLSIZEX").getOutput(0))  # Cell width X
		ymin = raster.extent.YMin  # Minimum Y value
		ymax = raster.extent.YMax  # Maximum Y value
		ydiff = float(arcpy.GetRasterProperties_management(
			raster, "CELLSIZEY").getOutput(0))  # Cell width Y (unique to PRISM)

		# Calculate the average precipitation for the month
		# Multiply by 1 to force the statistic to be calculated
		# Idk why this happens, but you can't get the mean w/out it
		PRCP = (1 * raster).mean

		# Load the temperature rasters
		tmin_raster_name = "PRISM_tmin_stable_4kmM2_{0}{1}_bil".format(
			year, month)
		tmin_raster_path = "{0}{1}/{1}.bil".format(
			prism_path, tmin_raster_name)
		tmin_raster = arcpy.Raster(tmin_raster_path)

		tmax_raster_name = "PRISM_tmax_stable_4kmM2_{0}{1}_bil".format(
			year, month)
		tmax_raster_path = "{0}{1}/{1}.bil".format(
			prism_path, tmax_raster_name)
		tmax_raster = arcpy.Raster(tmax_raster_path)

		tmean_raster_name = "PRISM_tmean_stable_4kmM2_{0}{1}_bil".format(
			year, month)
		tmean_raster_path = "{0}{1}/{1}.bil".format(
			prism_path, tmean_raster_name)
		tmean_raster = arcpy.Raster(tmean_raster_path)

		# Clip the temperature rasters
		arcpy.Clip_management(tmin_raster, bounds, 'tmin_{}{}'.format(
			year, month), la_shapefile, PRISM_NaN, "ClippingGeometry", "MAINTAIN_EXTENT")
		arcpy.Clip_management(tmax_raster, bounds, 'tmax_{}{}'.format(
			year, month), la_shapefile, PRISM_NaN, "ClippingGeometry", "MAINTAIN_EXTENT")
		arcpy.Clip_management(tmean_raster, bounds, 'tmean_{}{}'.format(
			year, month), la_shapefile, PRISM_NaN, "ClippingGeometry", "MAINTAIN_EXTENT")

		# Create TR raster as difference of tmax and tmin
		tr = arcpy.Raster("tmax_{}{}".format(year, month)) - \
			arcpy.Raster("tmin_{}{}".format(year, month))
		tc = arcpy.Raster("tmean_{}{}".format(year, month))

		# Create an ET table to store ET values
		empty_array = np.array([df_NaN] * ncol * nrow)
		yvals = np.arange(ymin, ymax, ydiff)
		flux_table = np.array(empty_array.reshape((nrow, ncol)))

		for row in range(0, nrow):
			# Get the latitude from the above code
			latitude = yvals[row]

			# Get the flux from our tools package
			flux = tools.daily_flux(month, 15, latitude)

			# Fill that row (i.e. latitude) with the flux
			flux_table[row, :] = [flux] * ncol

		# Get the mask for the temperature rasters
		# This is essentially the clip for the shapefile
		array = arcpy.RasterToNumPyArray(raster)
		masked = ma.masked_values(array, PRISM_NaN)
		mask = masked.mask

		# Apply the mask to the ET values (was just a rectangular grid before)
		flux_masked = ma.masked_array(flux_table, mask=mask)
		flux_masked = flux_masked.filled(PRISM_NaN)

		# Transform the masked array into a raster
		lower_left = arcpy.Point(xmin, ymin)
		flux_raster = arcpy.NumPyArrayToRaster(
			flux_masked, lower_left, xdiff, ydiff, PRISM_NaN)

		# Create the ET raster using Hargreaves equation
		ET_raster = 0.0023 * flux_raster * (tc + 17.8) * sa.SquareRoot(tr)
		ET = ET_raster.mean
		
		# Generate landuse raster
		landuse_resample = WaSSI.resample(landuse_raster, df_NaN, nrow, ncol)
		landuse_resample = np.transpose(landuse_resample)
		
		landuse_resample_masked = ma.masked_array(landuse_resample, mask=mask)
		landuse_resample_masked = landuse_resample_masked.filled(PRISM_NaN)
		
		w = arcpy.NumPyArrayToRaster(
			landuse_resample_masked, lower_left, xdiff, ydiff, PRISM_NaN)
			
		AET_raster = PRCP * (1 + w * ET / PRCP) / (1 + w * ET / PRCP + PRCP / ET)
		AET = AET_raster.mean

		# Set the values in our global table
		date = '{}/1/{}'.format(month, year)
		df['PRCP'][date] = PRCP
		df['ET'][date] = ET
		df['AET'][date] = AET

		# Clear all temporary data to prevent memory overflow
		# and so we can use the same names
		arcpy.Delete_management("ppt_{}{}".format(year, month))
		arcpy.Delete_management("tmin_{}{}".format(year, month))
		arcpy.Delete_management("tmax_{}{}".format(year, month))
		arcpy.Delete_management("tmean_{}{}".format(year, month))
		arcpy.Delete_management(tr)
		arcpy.Delete_management(flux_raster)
		arcpy.Delete_management(ET_raster)
		arcpy.Delete_management(w)

# Write the dataframe to file
df.to_csv('PRISM_processed.csv')
