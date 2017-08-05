import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
#from pandas.io.data import DataReader
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()

df = web.DataReader("NASDAQ:TSLA", "google", start, end)

#df=web.get_data_yahoo('TSLA',start,end)
print(df.tail())
style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)
df = web.DataReader('TSLA', "google", start, end)

df.to_csv('TSLA.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Close'].rolling(window=100,min_periods=0).mean()

df_ohlc=df['close'].resample('10D').ohlc()
df_volume=df['volume'].resample('10D').sum()


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])


plt.show()