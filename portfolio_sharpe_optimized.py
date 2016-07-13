import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def read_stock(stock, usecols=['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock),
		index_col='Date',
		parse_dates = True,
		usecols = usecols,
		na_values = ['nan']);

	df = df.rename(columns = {'Adj Close': stock})

	return df

def normalize(stockTable):
	return stockTable / stockTable.values[0]


def get_portfolio_negative_sharp(allocs, stockTable):
	std = np.asarray(stockTable.std().values)
	return_val = np.asarray(stockTable[-1:].values[0]) * allocs
	sharpe = -1 * sum((return_val / std) * allocs)
	return sharpe

def sumOne(n):
	return sum(n) - 1

def run():
	start_date="2010.01.01"
	end_date="2010.12.31"

	assetList = ['GLD', 'GOOG', 'AAPL', 'SPY']
	allocs = (0.25, 0.25, 0.25, 0.25)

	stockTable = pd.DataFrame(index = pd.date_range(start_date, end_date))

	for asset in assetList:
		stockTable = stockTable.join(read_stock(asset), how = 'inner')

	stockTable.sort_index(inplace = True)
	stockTable = normalize(stockTable)
	#stockTable = stockTable * allocs

	#print stockTable
	std = np.asarray(stockTable.std().values)

	return_val = np.asarray(pd.DataFrame(stockTable[-1:]).values[0]) * allocs

	sharpe = return_val / std

	print return_val
	print std
	print sharpe

	print sum(sharpe)

	#print get_portfolio_negative_sharp(allocs, stockTable)

	sharpe_minimized_allocs = spo.minimize(get_portfolio_negative_sharp, allocs,
							method = 'SLSQP',
							args = (stockTable,),
							bounds = ((0, 1),(0, 1),(0, 1),(0, 1)),
							constraints = ({'type' : 'eq', 'fun' : sumOne })
							)

	print sharpe_minimized_allocs

	#stockTable.plot()
	#plt.show()




if __name__  == '__main__':
	run()