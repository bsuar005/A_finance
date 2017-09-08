
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')  # Give nice white background with grid
from datetime import datetime

stocks = ['AAPL','GOOG','MSFT','AMZN']
end = datetime.now()

start = datetime(end.year-1,end.month,end.day)
main_df = web.DataReader(stocks, "google", start, end)['Close']
AAPL = main_df['AAPL']

A = 0
Z = 13
def RSI(stock):
    leny = (len(stock)) - 1
    leny2 = (len(stock)) - 15
    stock = stock[leny2:leny].diff()
    up = []
    down = []
    for x in stock:
        if x > 0:
            up.append(x)
        if x < 0:
            down.append(x)
    up = np.mean(up)
    down = np.mean(down)
    RSI = 100-(100/(1+(up/(down*-1))))

    return RSI
print(RSI(AAPL))
#for i in reversed(AAPL):
    #A+= 1
    #Z+=1
    #print(RSI(AAPL))



