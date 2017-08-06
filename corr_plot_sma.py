"""
Creates correlation plot

Author: Braulio Suarez
Date: 8/6/2017
"""

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns

from pandas import Series, DataFrame
from datetime import datetime

sns.set_style('whitegrid')  # Give nice white background with grid

stocks = ['AAPL', 'TEF', 'MSFT', 'TSLA']

end_date = datetime.now()
start_date = datetime(end_date.year - 1, end_date.month, end_date.day)

# Get ticker
main_df = web.DataReader(stocks, "google", start_date, end_date)['Close']
rets = main_df.pct_change().dropna(inplace=True)

# creating heat map
corr = main_df.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True  # something
cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, center=0, annot=True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

for idx, stock in enumerate(stocks):
    plt.subplot(len(stocks), 1, idx + 1)
    plt.ylabel(stock)
    stock = main_df.loc[:, [stock]]
    plt.plot(stock)

    stock['10_days'] = stock[[0]].rolling(window=10, center=False).mean()
    stock['20_days'] = stock[[0]].rolling(window=20, center=False).mean()
    stock['50_days'] = stock[[0]].rolling(window=50, center=False).mean()
    plt.plot(stock[['10_days', '20_days', '50_days']], linestyle='--')
    plt.legend(['Close', '10_days', '20_days', '50_days'], loc=2)

plt.show()
