#
# Pull data from Quandl API
# Conveniently returns pandas dataframe
#
import urllib2
import numpy as np
import pandas as pd
import Quandl

from authkey import key

# get soybean oil futures
def pullSoybeanOilFutures():
	return Quandl.get("CHRIS/CME_BO1", authtoken=key)
# get soybean futures
def pullSoybeanFutures():
	return Quandl.get("CHRIS/CME_S1", authtoken=key)
# get soybean oil CTR
def pullSoybeanOilCTR():
	return Quandl.get("CFTC/BO_F_ALL", authtoken=key)
# get soybean CTR
def pullSoybeanCTR():
	return Quandl.get("CFTC/S_F_ALL", authtoken=key)