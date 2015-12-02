import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import graph
import pullquandl
import sys

# Debugging function to print pandas obj
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

def plotSoybeanData():
	soyF_df = pullquandl.pullSoybeanFutures()
	soyCTR_df = pullquandl.pullSoybeanCTR() 
	graph.draw(soyF_df, 'Total Long Short Ratio Of Soybean Future since 2006', 'Total Longs/Total Shorts', \
		soyCTR_df, 'Cumulative Daily Returns For Soybean since 1959', 'Cumulative Daily Returns For Soybean')

def plotSoybeanOilData():
	soyOilF_df = pullquandl.pullSoybeanOilFutures()
	soyOilCTR_df = pullquandl.pullSoybeanOilCTR()
	graph.draw(soyOilF_df, 'Total Long Short Ratio Of Soybean Oil Future since 2006', 'Total Longs/Total Shorts', \
		soyOilCTR_df, 'Cumulative Daily Returns For Soybean Oil since 1959', 'Cumulative Daily Returns For Soybean Oil')

# prints 0.621154007969
# strong linear relationship - expected since complements in production
def calculateCorrelationCoefficient():
	soyF_df = pullquandl.pullSoybeanFutures()
	soyF_df['dailyReturns'] = (soyF_df['Last'] - soyF_df['Open'])/soyF_df['Open']
	soyOilF_df = pullquandl.pullSoybeanOilFutures()
	soyOilF_df['dailyReturns'] = (soyOilF_df['Last'] - soyOilF_df['Open'])/soyOilF_df['Open']
	print(soyF_df['dailyReturns'].corr(soyOilF_df['dailyReturns'], method='pearson'))

if __name__ == '__main__':
	argIn = sys.argv[1]
	if(argIn == 'soybean'):
		plotSoybeanData()
	elif(argIn == 'soybeanoil'):
		plotSoybeanOilData()
	elif(argIn == 'correlate'):
		calculateCorrelationCoefficient()
	else:
		print("Enter valid command line argument")