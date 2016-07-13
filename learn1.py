import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

def read_stock(stock, usecols = ['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock), index_col='Date',
			parse_dates=True,
			usecols = usecols,
			na_values = ['nan'])
	df = df.rename(columns={'Adj Close' : stock})
	return df

def run():
	start_date = '2014-01-01'
	end_date = '2015-12-31'

	df = pd.DataFrame(index=pd.date_range(start_date, end_date))
	my_stocks = ['AAPL', 'GOOG', 'IBM', 'CRM'];

	for stock in my_stocks:
		df = df.join(read_stock(stock), how='inner')

	df.sort_index(inplace=True)

	daily = df[1:] / df[:-1].values
	normalized = df / df.values[1]

	fig, (ax1, ax2, ax3,) = plt.subplots(3, sharex=True)

	df.plot(ax=ax1, title='Historical Prices')
	normalized.plot(ax=ax2, title='Normalized Prices')
	daily.plot(ax=ax3, title='Daily Returns')
	
	plt.show()



if __name__ == '__main__':
	run()