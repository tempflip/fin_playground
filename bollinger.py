#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt

### bla blak

def read_stock(stock, usecols = ['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock), index_col='Date',
			parse_dates=True,
			usecols = usecols,
			na_values = ['nan'])
	df = df.rename(columns={'Adj Close' : stock})
	return df

def rolling_mean(df, window=20):
	return pd.rolling_mean(df, window=window)

def rolling_std(df, window=20):
	return pd.rolling_std(df, window=20)

def run():
	print 'ok'
	start_date = '2010-01-01'
	end_date = '2016-06-03'
	dates = pd.date_range(start_date, end_date)

	df1 = pd.DataFrame(index=dates)

	my_stocks = ['SPY', 'GLD', 'AAPL', 'GOOG', 'IBM']
	#my_stocks = ['SPY']
	for stock in my_stocks:
		stock_df = read_stock(stock)
		df1 = df1.join(stock_df, how='inner')

	df1.sort_index(inplace=True)
	print df1

	spy = df1.loc['2015-01-01':,'SPY']

	spy_rm1 = rolling_mean(spy, window = 30)
	spy_rm2 = rolling_mean(spy, window = 50)
	spy_rstd = rolling_std(spy_rm1)

	boll_up = spy_rm1 + 2 * spy_rstd;
	boll_down = spy_rm1 - 2 * spy_rstd;

	ax = spy.plot(title='Rolling Means', label='SPY')


	spy_rm1.plot(ax = ax, label = 'Rolling Mean 20')
	#spy_rstd.plot(ax=ax)	
	boll_up.plot(ax=ax)
	boll_down.plot(ax=ax)


	#ax3 = spy_rm2.plot(ax = ax2, label = 'Rolling Mean 50')
	
	ax.set_xlabel('Date')
	ax.set_ylabel('Price')

	#df1.plot()
	plt.show()
	

if __name__ == '__main__':
	run()



