import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas_datareader import data
 
#download Apple price data into DataFrame
apple = data.DataReader('KO', 'yahoo',start='1/1/2017')
 

days = (apple.index[-1] - apple.index[0]).days

apple['Returns'] = apple['Adj Close'].pct_change()

print(apple)
apple['Returns'].plot(kind='hist',figsize=(8,5),title='Daily Return Distribution',bins=50)

plt.show()

