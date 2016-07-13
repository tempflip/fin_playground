import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


def read_stock(stock, usecols=['Date', 'Close', 'Volume']):
	df = pd.read_csv("{}.csv".format(stock),
		index_col="Date",
		parse_dates=True,
		usecols=usecols,
		na_values=['nan']
	)
	return df


def run():
	df = read_stock('BTC_DAILY')
	df.sort_index(inplace=True)

	df['DR'] = df['Close'][1:] / df['Close'][:-1].values - 1

	print df




	fig, (ax1, ax2) = plt.subplots(2, sharex=True)


	ax1.set_title('Close and DR')
	ax1.plot(df['DR'], 'r')

	ax11 = ax1.twinx()	
	ax11.plot(df['Close'])	

	ax2.set_title('Volume and DR')
	ax2.plot(df['Volume'])

	ax22 = ax2.twinx()
	ax22.plot(df['DR'], 'r')
	plt.show()




if (__name__ == '__main__'):
	run();
