import arcpy
import numpy as np
import numpy.ma as ma

# Set default land-use w values
w_val = {
	"21": 1.4,
	"22": 1.0,
	"23": 0.6,
	"24": 0.4,
	"31": 0.0,
	"41": 2.8,
	"42": 2.8,
	"43": 2.8,
	"52": 2.0,
	"71": 2.0,
	"81": 2.0,
	"82": 2.0,
	"90": 2.0,
	"95": 2.0,
}

def resample(landuse_raster, df_NaN, nrow, ncol):
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