#from pandas.io.data import DataReader
from pandas_datareader import data
from datetime import datetime

aapl = data.DataReader('AAPL', 'yahoo', '1980-01-01')
print(aapl.til())

aapl.to_csv('/Users/chrislattanzio/Python/Mkt_Data/aapl_data.csv')