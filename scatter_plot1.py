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
	df = df.join(read_stock('AAPL'), how = 'inner')
	df = df.join(read_stock('FB'), how = 'inner')


	df.sort_index(inplace=True)



	daily = df[1:] / df[:-1].values -1

	beta, alpha = np.polyfit(daily.SPY, daily.GOOG, 1)

	print 'Beta: {}, Alpha: {}'.format(beta, alpha)

	

	daily.plot(kind='scatter', x = 'SPY', y = 'GOOG')
	plt.plot(daily.SPY, beta * daily.SPY + alpha, '-', color = 'red')

	#daily.SPY.hist(bins=20, label = 'SPY')
	#daily.GOOG.hist(bins=20, label = 'GOOG')

	plt.show()

	print daily.corr(method='pearson')







if __name__ == '__main__':
	run()