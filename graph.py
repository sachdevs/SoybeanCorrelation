import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pullquandl

def draw(futureSeries, ftitle, fylabel, CTRseries, ctitle, cylabel):
	futureSeries['dailyReturns'] = (futureSeries['Last'] - futureSeries['Open'])/futureSeries['Open']
	cumDailyReturns = futureSeries['dailyReturns'].cumsum()

	lrRatioSoy = CTRseries['Total Reportable Longs'] / CTRseries['Total Reportable Shorts']

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
