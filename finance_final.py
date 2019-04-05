import math
import numpy as np
import csv
import matplotlib.pyplot as plt

N=30
U=0.0005
D=-0.0005
capital=1000

def myStrategy01(pastData, N, U, D):
    u=0#miu
    s=0#sigma
    sha_rat=0#sharp ratio
    action=0
    if len(pastData)<N+1:
        return 0,0
    # N points
    wdData=pastData[-N:]
    # returns
    ret=np.zeros(N)
    ret[1:]=np.divide(wdData[1:],wdData[:-1])-1
    #miu
    u = np.sum(ret)/N
    #sigma
    s = np.sqrt(np.sum(np.square(ret-u))/(N-1))
    #sharpe ratio
    if s!=0:
        sha_rat=u/s
    if sha_rat>U:
        action=1
    elif sha_rat<D:
        action=-1
    elif D<=sha_rat<=U:
        action=0
    else:
        print("Something's wrong.")
    return action, sha_rat

#read the csv file
with open('spy.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates=[]
    for col in readCSV:
        date = col[5]
        dates.append(date)
adjClose=[]
for i in range(1,len(dates),1):
    adjClose.append(float(dates[i]))
#initialize array
dataCount=len(adjClose)
suggestedAction=np.zeros([dataCount,1])
ratio=np.zeros([dataCount,1])
unit=np.zeros([dataCount,1])
total=np.zeros([dataCount,1])
realAction=np.zeros([dataCount,1])
total[0]=capital
for i in range(0,dataCount,1):
    suggestedAction[i], ratio[i]=myStrategy01(adjClose[:i], N, U, D)
    currPrice=adjClose[i]
    if i>0:
        unit[i]=unit[i-1]
    if suggestedAction[i]==1:
        if unit[i]==0:#BUY
            unit[i]=capital/currPrice
            capital=0
            realAction[i]=1
    elif suggestedAction[i]==-1:
        if unit[i]>0:#SELL
            capital=unit[i]*currPrice
            unit[i]=0
            realAction[i]=-1
    else:#suggestedAction[i]=0 or unknown action 
        print('do nothing')
    total[i]=capital+unit[i]*currPrice
#print the result
print(np.sum(realAction==1))
print(np.sum(realAction==-1))
print(float(total[-1]))
#plot
fig, ax = plt.subplots(5)
x = [i for i in range(0,dataCount)]
ax[0].plot(x,adjClose)
ax[0].set_title('Adj Close')
ax[1].plot(x,ratio)
ax[1].set_title('Sharpe ratio')
ax[2].plot(x,realAction)
ax[2].set_title('Action')
ax[3].plot(x,unit)
ax[3].set_title('Stock holdings')
ax[4].plot(x,total)
ax[4].plot(x,1000*np.ones([dataCount,1]),color='r')
ax[4].set_title('Total asset')
plt.tight_layout()
plt.show()



