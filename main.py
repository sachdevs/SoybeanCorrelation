import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import graph
import pullquandl

# Debugging function to print pandas obj
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

soyF_df = pullquandl.pullSoybeanFutures()
soyCTR_df = pullquandl.pullSoybeanCTR() 
graph.draw(soyF_df, 'Total Long Short Ratio Of Soybean Future since 2006', 'Total Longs/Total Shorts', \
	soyCTR_df, 'Cumulative Daily Returns For Soybean since 1959', 'Cumulative Daily Returns For Soybean')

soyOilF_df = pullquandl.pullSoybeanOilFutures()
soyOilCTR_df = pullquandl.pullSoybeanOilCTR()
graph.draw(soyOilF_df, 'Total Long Short Ratio Of Soybean Oil Future since 2006', 'Total Longs/Total Shorts', \
	soyOilCTR_df, 'Cumulative Daily Returns For Soybean Oil since 1959', 'Cumulative Daily Returns For Soybean Oil')
