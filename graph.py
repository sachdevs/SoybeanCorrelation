import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pullquandl

def draw(futureSeries, ftitle, fylabel, CTRseries, ctitle, cylabel):
	# caluclate daily returns
	futureSeries['dailyReturns'] = (futureSeries['Last'] - futureSeries['Open'])/futureSeries['Open']
	# create cumulatively summed series
	cumDailyReturns = futureSeries['dailyReturns'].cumsum()

	# calculate long short ratio
	lrRatioSoy = CTRseries['Total Reportable Longs'] / CTRseries['Total Reportable Shorts']

	# graph both series
	# make matplotlib window larger
	plt.figure(figsize=(4*3.13,2.5*3.13))
	plt.subplot(1, 2, 1)
	plt.title(ftitle)
	plt.ylabel(fylabel)
	plt.xlabel('Date')
	plt.plot(lrRatioSoy.index, lrRatioSoy)

	plt.subplot(1, 2, 2)
	plt.title(ctitle)
	plt.ylabel(cylabel)
	plt.xlabel('Date')
	plt.plot(cumDailyReturns.index, cumDailyReturns)
	plt.show()
