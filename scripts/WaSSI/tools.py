import arcpy
import numpy as np
import numpy.ma as ma
import pandas as pd

# Solar Constant
# --------------
# Description: Average flux on a plane perpendicular 
# to the solar beam at the upper surface of the atmosphere
#
# Units: MJ m^-2
I_sc = 4.921

# Day Angle
# ---------
# Description: The position of earth in its orbit as a 
# function of the day
# 
# Units: -
def day_angle(month, day):
	"""Returns the day angle given a month and day.
	"""
	
	# Construct a Series with values 1-365 mapped to January 1 - December 31
	df = pd.Series(range(1,366), index=pd.date_range(start='1/1/2017', end='12/31/2017'))
	
	# Get the day number by indexing the series
	day_number = df['{}/{}/2017'.format(month,day)]
	
	return 2 * np.pi * (day_number - 1) / 365

# Eccentricity Correction
# -----------------------
# Description: The correction given Earth's ellipitcal orbit
#
# Units: -
def eccentricity_correction(day_angle):
	"""Returns the eccentricity correction given the day angle.
	"""
	return 1.000110 + 0.034221 * np.cos(day_angle) + 0.001280 * np.sin(day_angle) \
			+ 0.000719 * np.cos(2 * day_angle) + 0.000077 * np.sin(2 * day_angle)
	
# Declination
# -----------
# Description: The latitude at which the sun is directly overhead at noon
# 
# Units: Latitude in degrees
def declination(day_angle):
	"""Returns the declination given the day angle.
	"""
	return (180 / np.pi) * (0.006918 - 0.399912 * np.cos(day_angle) + 0.070257 * np.sin(day_angle) \
			- 0.006758 * np.cos(2 * day_angle) + 0.000907 * np.sin(2 * day_angle) - 0.002697 * np.cos(3 * day_angle) \
			+ 0.00148 * np.sin(3 * day_angle))

def daily_flux(month, day, latitude):
	"""Returns the daily solar radiation flux.
	"""
	
	# Set the parameters
	dag = day_angle(month, day)
	dec = np.deg2rad(declination(dag))
	lat = np.deg2rad(latitude)
	
	# Eccentricity correction
	Ec = eccentricity_correction(dag)
	
	# Earth's angular velocity (rad/hr)
	vel = np.deg2rad(15)
	# Hour of sunset
	Ths = np.arccos(-np.tan(dec) * np.tan(lat)) / vel
	 
	return 2 * I_sc * Ec * (np.cos(dec) * np.cos(lat) * np.sin(vel * Ths) / vel \
			+ np.sin(dec) * np.sin(lat) * Ths)

# Set default land-use w values
w_val = {
	"21": 0.91,	# Developed, Open Space 	     <20% developed
	"22": 0.75,	# Developed, Low Intensity 	   20-49% developed
	"23": 0.66,	# Developed, Medium Intensity  50-79% developed
	"24": 0.25,	# Developed, High Intensity	  80-100% developed
	"31": 0.1,	# Barren Land
	"41": 2.8,	# Deciduous Forest
	"42": 2.8,	# Evergreen Forest
	"43": 2.8,	# Mixed Forest
	"52": 1.0,	# Shrub/Scrub
	"71": 1.0,	# Grassland/Herbaceous
	"81": 1.0,	# Pasture/Hay
	"82": 1.0,	# Cultivated Crops
	"90": 1.0,	# Woody Wetlands
	"95": 1.0,	# Emergent Herbaceous Wetlands
}

def w_resample(landuse_raster, df_NaN, nrow, ncol):
	# Get land use raster bounds
	landuse_width = int(landuse_raster.width)
	landuse_height = int(landuse_raster.height)

	landuse_arr = arcpy.RasterToNumPyArray(landuse_raster)

	# Create AET array
	landuse_resample = np.array([df_NaN] * ncol * nrow).reshape((ncol, nrow))

		# Step through each land use segment to get w value and
		# calculate AET (Actual Evapotranspiration)
	landuse_xdiff = landuse_width / ncol
	landuse_ydiff = landuse_height / nrow
	for x in range(ncol):
		for y in range(nrow):
			# Get the subsection of the landuse raster for this pixel
			xstart = x * landuse_xdiff
			xend   = xstart + landuse_xdiff
			ystart = y * landuse_ydiff
			yend   = ystart + landuse_ydiff
			quadrant = landuse_arr[xstart:xend, ystart:yend]
			
			# Create mask to get accurate mean
			masked_quadrant = ma.masked_outside(quadrant, 1, 100)
			masked_quadrant = ma.compressed(masked_quadrant)
			bincount = np.bincount(masked_quadrant)
			
			count = 0
			total_w = 0
			for w in w_val:
				if bincount.size > int(w): 
					val = w_val[w]
					bin = bincount[int(w)]
					count += bin
					total_w += val * bin
			
			if count > 0:
				this_w = total_w / count
			else:
				this_w = 0.0
			
			landuse_resample[x, y] = this_w
	
	return landuse_resample