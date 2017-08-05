
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')  # Give nice white background with grid
from datetime import datetime



tech_list = ['AAPL','GOOG','MSFT','AMZN']
end = datetime.now()

start = datetime(end.year-1,end.month,end.day)
for stock in tech_list:
    globals()[stock] = web.DataReader("NASDAQ:TSLA", "google", start, end)

ma_day = [10, 20, 50]

for ma in ma_day:
    column_name = "MA for {} days".format(str(ma))
    AAPL[column_name] = AAPL['Close'].rolling(window=ma,center=False).mean()

AAPL[['Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))
plt.show()

