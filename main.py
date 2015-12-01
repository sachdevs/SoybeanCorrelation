import urllib2
import numpy as np
import pandas as pd
import Quandl

import time
from authkey import key
# import datetime

# import pylab
# import matplotlib.pyplot as plt
# import matplotlib.ticker as mticker
# import matplotlib.dates as mdates
# import sys

# Debugging function to print pandas obj
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

#
# Pull data from Quandl
#
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

#Initialize Pandas objects of scraped data
soyOilF = pullSoybeanOilFutures()
soyF = pullSoybeanFutures()
soyOilCTR = pullSoybeanOilCTR()
soyCTR = pullSoybeanCTR() 

print_full(soyCTR)