import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def read_stock(stock, usecols=['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock),
		index_col='Date',
		parse_dates = True,
		usecols = usecols,
		na_values = ['nan']);

	df = df.rename(columns = {'Adj Close': stock})

	return df

def build_portfolio(start_date = '2013-01-01',
	end_date = '2016-06-03',
	stocklist = ['GOOG', 'AAPL', 'SPY'], 
	allocs = [0.4, 0.4, 0.2],
	start_value = 1000):
	
	df = pd.DataFrame(index=pd.date_range(start_date, end_date))

	for stock in stocklist:
		df = df.join(read_stock(stock), how = 'inner')

	df.sort_index(inplace=True)

	normalized = df / df.values[0]
	allocated = normalized * allocs
	portfolio_value = allocated * start_value

	portfolio_value['VAL'] = pd.Series(0, index=portfolio_value.index)
	for stock in stocklist:
		portfolio_value.VAL = portfolio_value.VAL + portfolio_value[stock]

	return portfolio_value

def add_rand(n, step = 0.1):
	return n + random.random() * step * 2 - step

def run():

	high = 0
	for i in range(1000):
		allocs = [random.random() for n in range(3)]
		allocs = [n / sum(allocs) for n in allocs]

		port = build_portfolio(allocs = allocs)
		if (port.VAL[-1] > high):
			high = port.VAL[-1]
			print "{} \t {} \t {}".format(i, high, allocs)





if __name__ == '__main__':
	run()