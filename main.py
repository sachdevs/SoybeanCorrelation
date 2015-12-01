import urllib2
import numpy as np
import pandas as pd
import Quandl
import pullquandl

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

#Initialize Pandas objects of scraped data
# soyOilF = pullquandl.pullSoybeanOilFutures()
# soyF = pullquandl.pullSoybeanFutures()
# soyOilCTR = pullquandl.pullSoybeanOilCTR()
soyCTR = pullquandl.pullSoybeanCTR() 

print_full(soyCTR)