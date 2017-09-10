
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')  # Give nice white background with grid
from datetime import datetime

Main_DF_Stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
Stock_Choice='AAPL'

end = datetime.now()

start = datetime(end.year-1,end.month,end.day)
main_df = web.DataReader(Main_DF_Stocks, "google", start, end)['Close']
stock = main_df[Stock_Choice]


#need the length of time period analyzed


#we get the dif between 14 days, if positive goes in up, if negative in down

#going from the latest day it looks back 14 days, subtracts 1 from len to go back a day for each iteration

def RSI_14(days):
    RSI_list = []
    stock = main_df[Stock_Choice]
    leny = (len(stock))
    leny2 = (len(stock)) - days

    for i in reversed(stock[days:]):
        RSI_list.append(RSI(stock,leny,leny2))
        leny-=1
        leny2-=1

    #since it goes backwards will give error on first days since it lacks enough data ie -2 index
    RSI_list2=[0]*days
    #revers list so it can merged with first index as last date
    for i in reversed(RSI_list):
        RSI_list2.append(i)

    #make AAPL a dataframe not a series
    stock = main_df[['AAPL']]
    #set index to colums so it can merge
    stock.reset_index(inplace=True)
    #make list into a series
    RSI_list2=Series(RSI_list2)
    RSI_list2.rename('RSI',inplace=True)
    #merge
    Final_Result=pd.concat([stock, RSI_list2], axis=1)
    Final_Result=Final_Result.set_index('Date')
    Final_Result.drop('AAPL', axis=1, inplace=True)
    lenny3=len(Final_Result)-1

    print(Final_Result)
    ax3= Final_Result[days:].plot(kind='line')
    ax3.set_title('{} {} day RSI is {}'.format(Stock_Choice,days+1,round(Final_Result['RSI'][lenny3],2)))
    plt.axhline(y=30,xmin=0,xmax=3,c="red",linewidth=1,zorder=1)
    plt.axhline(y=70,xmin=0,xmax=3,c="red",linewidth=1,zorder=1)


def RSI(stock,leny,leny2):
    #needs to be in reverse
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
    #do the RSI formula and returns that days RSI
    RSI = 100-(100/(1+(up/(down*-1))))

    return RSI

RSI_14(13)
RSI_14(7)
plt.show()