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

	df = pd.DataFrame(index=pd.date_range(start_date, end_date))
	df = df.join(read_stock('SPY'), how = 'inner')
	df = df.join(read_stock('GOOG'), how = 'inner')


	df.sort_index(inplace=True)


	daily = df[1:] / df[:-1].values -1

	daily.SPY.hist(bins=20, label = 'SPY')
	daily.GOOG.hist(bins=20, label = 'GOOG')
	
	mean = daily.mean()
	std = daily.std()




	plt.axvline(mean.GOOG, color='w', linestyle='dashed', linewidth=2)

	plt.axvline(mean.GOOG, color='r', linestyle='dashed', linewidth=2)

	#plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
	#plt.axvline(-1 * std, color='r', linestyle='dashed', linewidth=2)

	#plt.axvline(2 * std, color='g', linestyle='dashed', linewidth=2)
	#plt.axvline(-2 * std, color='g', linestyle='dashed', linewidth=2)

	plt.show()


	#print daily.kurtosis()







if __name__ == '__main__':
	run()