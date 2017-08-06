
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')  # Give nice white background with grid
from datetime import datetime

stocks = ['AAPL','TEF','MSFT','TSLA']
end = datetime.now()

start = datetime(end.year-1,end.month,end.day)
main_df = web.DataReader(stocks, "google", start, end)['Close']
rets = main_df.pct_change()
rets = rets.dropna()


corr = main_df.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, annot=True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

fig = plt.figure()
ma_day = [10, 20, 50]
counter=len(stocks)
i=1
for stock in stocks:
    plt.ylabel(stock)
    stock=main_df[[stock]]
    plt.subplot(counter, 1, i)
    plt.plot(stock)
    stock['10_days']=stock[[0]].rolling(window=10,center=False).mean()
    stock['20_days'] = stock[[0]].rolling(window=20, center=False).mean()
    stock['50_days'] = stock[[0]].rolling(window=50, center=False).mean()
    plt.plot(stock[['10_days', '20_days', '50_days']])
    i=i+1

plt.show()
