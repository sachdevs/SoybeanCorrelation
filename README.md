# SoybeanCorrelation
How to run:
```
$ python main.py [correlate/soybean/soybeanoil]
```
#####correlate
Prints pearson correlation coefficient for soybean daily returns vs soybean oil daily returns. Value is around 0.62 which is a strong linear relation (as expected since these commodities are complements in production).

#####soybean/soybeanoil
Graphs soybean/ soybean oil future daily returns (cumulative) and Long/Short ratios.

##Comments
The daily returns are calculated a slightly simplified method, should be (at time t) (Last(t) - Last(t-1)) / Last(t-1) <br>
Done as coding challenge for [Alpha Parity LLC](http://www.alphaparity.com).