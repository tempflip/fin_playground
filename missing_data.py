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
	start_date='1993-01-01'
	end_data = '2016-06-01'

	dates = pd.date_range(start_date,end_data)

	df = pd.DataFrame(index=dates)
	df = df.join(read_stock('FB'), how = 'inner')
	df = df.join(read_stock('SPY'), how = 'inner')

	df = df.sort_index()
	print df

	df.plot()

	plt.show()



if __name__ == '__main__':
	run();