#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt

def read_stock(stock, usecols = ['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock), index_col='Date',
			parse_dates=True,
			usecols = usecols,
			na_values = ['nan'])
	df = df.rename(columns={'Adj Close' : stock})
	return df


def run():
	print 'ok'
	start_date = '2010-01-01'
	end_date = '2016-06-03'
	dates = pd.date_range(start_date, end_date)

	df1 = pd.DataFrame(index=dates)

	my_stocks = ['SPY', 'GLD', 'AAPL', 'GOOG', 'IBM']

	for stock in my_stocks:
		stock_df = read_stock(stock)
		df1 = df1.join(stock_df, how='inner')

	df1.sort_index(inplace=True)

	#for date in df1.index:
	#	for stock in my_stocks:
	#		df1.loc[date][stock] = df1.loc[date][stock] / df1.loc[ df1[stock].index[0] ][stock]



	#print df1.ix['2016-05-06' : '2016-05-19', ['GLD', 'GOOG']]
	
	df1 = df1 / df1.ix[0,:]

	graph = df1.plot(title="Stocks")
	graph.set_xlabel = 'Date'
	graph.set_ylabel = 'Price'

	plt.show()


if __name__ == '__main__':
	run()



