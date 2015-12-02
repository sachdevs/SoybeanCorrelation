# SoybeanCorrelation
How to run:
First create a file called authkey.py and write
```
key = "YOUR_KEY_HERE"
```
then run this in terminal making sure you have matplotlib, scipy stack, pandas, and Quandl API installed (all packages can be installed through pip unless you are on windows, in which case download anaconda distribution of python)
```
$ python main.py [correlate/soybean/soybeanoil]
```
#####correlate
Prints pearson correlation coefficient for soybean daily returns vs soybean oil daily returns. Value is around 0.62 which is a strong linear positive relation (I would think this makes sense since these commodities are complements in production).

#####soybean/soybeanoil
Graphs soybean/ soybean oil future daily returns (cumulative) and Long/Short ratios.

##Comments
The daily returns are calculated a slightly simplified method, should be (at time t) (Last(t) - Last(t-1)) / Last(t-1) <br>
Done as coding challenge for [Alpha Parity LLC](http://www.alphaparity.com).