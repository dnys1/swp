import numpy as np
import pandas as pd

# Solar Constant
# --------------
# Description: Average flux on a plane perpendicular 
# to the solar beam at the upper surface of the atmosphere
#
# Units: MJ m^-2
I_sc = 118.1

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

# Zenith Angle
# ------------
# Description: Angle between line from an observer on earth to the snun
# and a line extending from the observer, perpendicular to Earth
# 
# Units: Degrees
def zenith_angle(day_angle, latitude):
	"""Returns the zenith angle given the day angle, latitude (degrees).
	"""
	# Declination in radians
	dec = np.deg2rad(declination(day_angle))
	# Latitude in radians
	lat = np.deg2rad(latitude)
	
	return np.arccos(np.sin(dec) * np.sin(lat) + np.cos(dec) * np.cos(dec))

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