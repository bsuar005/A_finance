
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
rets = main_df.pct_change()
rets = rets.dropna()


stock='GOOG'
days = 365
dt = 1/days
mu = rets.mean()[stock]
sigma = rets.std()[stock]
start_price=main_df[stock][-1]

def stock_monte_carlo(start_price, days, mu, sigma):
    price = np.zeros(days)
    price[0] = start_price

    shock = np.zeros(days)
    drift = np.zeros(days)

    for x in range(1, days):
        shock[x] = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt))

        drift[x] = mu * dt

        price[x] = price[x - 1] + (price[x - 1] * (drift[x] + shock[x]))

    return price

runs = 10000

simulations = np.zeros(runs)

for run in range(runs):
    simulations[run] = stock_monte_carlo(start_price,days,mu,sigma)[days-1]

q = np.percentile(simulations,1)

plt.hist(simulations,bins=200)

# Starting Price
plt.figtext(0.6,0.8, s="Start price: $%.2f" %start_price)

# Mean Ending Price
plt.figtext(0.6,0.7, "Mean final price: $%.2f" % simulations.mean())

#Variance of the price (within 99% confidence interval)
plt.figtext(0.6,0.6, "VaR(0.99): $%.2f" % (start_price - q,))

# Display 1% quantile
plt.figtext(0.15,0.6, "q(0.99): $%.2f" % q)

# Plot a line at the 1% quantile result
plt.axvline(x=q, linewidth=4,color='r')

plt.title(u"Final price distribution for Google Stock after %s days" %days, weight='bold')

plt.show()
