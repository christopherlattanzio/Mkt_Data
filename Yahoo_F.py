#from pandas.io.data import DataReader
from pandas_datareader import data
from datetime import datetime
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

aapl = data.DataReader('AAPL', 'yahoo', '2015-01-01')

aapl['Moving Avg'] = Series.rolling(aapl['Adj Close'], 20).mean()

#pd.rolling_mean(aapl['Adj Close'], 20)
#print(aapl.tail())

plot1 = pd.DataFrame(aapl, columns=['Adj Close','Moving Avg'])

print(plot1.tail())

plt.plot(plot1)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Closing Price')
plt.show()



#aapl.to_csv('/Users/chrislattanzio/Python/Mkt_Data/aapl_data.csv')