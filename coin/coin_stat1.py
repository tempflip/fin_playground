import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

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

	## linear
	n = 150

	my_array = np.arange(len(df))
	df['my'] = my_array

	regr = linear_model.LinearRegression()
	regr.fit(df['my'].values[:n].reshape(n, 1), df['Close'].values[:n])

	df['regr'] = [regr.predict(x)[0] for x in df['my'].values]

	## polynominal
	poly = PolynomialFeatures(degree=6)
	x_ = poly.fit_transform(df['my'].values.reshape(len(df), 1))


	regr_poly = linear_model.LinearRegression()
	regr_poly.fit(x_, df['Close'].values)

	df['regr2'] =  [regr_poly.predict(x)[0] for x in x_]

	print df

	fig, (ax1, ax2) = plt.subplots(2, sharex=True)

	ax1.set_title('Close and DR')
	ax1.plot(df['DR'], 'r')

	ax11 = ax1.twinx()	
	ax11.plot(df['Close'])	
	ax11.plot(df['regr'])
	ax11.plot(df['regr2'])

	ax2.set_title('Volume and DR')
	ax2.plot(df['Volume'])

	ax22 = ax2.twinx()
	ax22.plot(df['DR'], 'r')
	plt.show()




if (__name__ == '__main__'):
	run();
