import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_stock(stock, usecols=['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock),
		index_col='Date',
		parse_dates = True,
		usecols = usecols,
		na_values = ['nan']);

	df = df.rename(columns = {'Adj Close': stock})

	return df

def run():
	start_date = '2000-01-01'
	end_date = '2016-06-03'
	dates = pd.date_range(start_date, end_date)
	df = pd.DataFrame(index = dates).join(read_stock('GOOG'), how='inner')
	df = df.join(read_stock('AAPL'), how='inner')
	df = df.join(read_stock('SPY'), how='inner')

	df.sort_index(inplace=True)

	daily = df.copy()

	daily[1:] = df[1:] / df[:-1].values - 1
	
	daily = daily[1:]
	
	df_norm = df / df.max()



	cum_return = df / df[0:1].values[0]

	df.plot()
	cum_return.plot()

	plt.show()
	#ax = df_norm.plot()
	#print cum_return


	
	
	#plt.show()


if __name__ == '__main__':
	run()