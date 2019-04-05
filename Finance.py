import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas_datareader import data
import datetime as dt
 
micro = data.DataReader('MSFT', 'yahoo',start='1/1/2000',end=dt.date.today())
days = (micro.index[-1] - micro.index[0]).days
cagr = ((((micro['Adj Close'][-1]) / micro['Adj Close'][1])) ** (365.0/days)) - 1
print ('CAGR =',str(round(cagr,4)*100)+"%")
mu = cagr
micro['Returns'] = micro['Adj Close'].pct_change()
vol = micro['Returns'].std()*sqrt(252)
print ("Annual Volatility =",str(round(vol,4)*100)+"%")
result = []
S = micro['Adj Close'][-1]
T = 252

for i in range(1000):
    daily_returns=np.random.normal(mu/T,vol/sqrt(T),T)+1
    price_list = [S] 
    for x in daily_returns:
        price_list.append(price_list[-1]*x)
    plt.plot(price_list)
    result.append(price_list[-1]) 
plt.show()
plt.hist(result,bins=50)
plt.axvline(np.percentile(result,5), color='r', linestyle='dashed', linewidth=2)
plt.axvline(np.percentile(result,95), color='r', linestyle='dashed', linewidth=2)
plt.show()
