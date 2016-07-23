import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

def read_stock(stock, usecols = ['Date', 'Adj Close']):
	df = pd.read_csv('{}.csv'.format(stock), index_col='Date',
			parse_dates=True,
			usecols = usecols,
			na_values = ['nan'])
	df = df.rename(columns={'Adj Close' : stock})
	return df

class Model:
	def __init__(self):
		self.model = None
		self.description = "i'm an untrained model"
		pass

	def __str__(self):
		return self.description

	def train(self):
		pass

	def predict(self, x):
		pass

class Linear_Model(Model):
	def __init__(self):
		Model.__init__(self)
		pass

	def train(self, training_x_matrix, training_y_matrix, degree=1):
		self.degree = degree
		# creating a 1...n space len of the training matrix
		my_space = np.arange(len(training_x_matrix)).reshape(-1,1) 
		poly = PolynomialFeatures(degree=self.degree)
		# polynominal features of the space
		my_space_features = poly.fit_transform(my_space) 

		# training the model
		regr = linear_model.LinearRegression()
		regr.fit(my_space_features, training_y_matrix)
		self.model = regr

		self.description = "i'm a linear model of {} degree".format(self.degree)

	def predict(self, x):
		## as it is trained on polynominal features, we need to transform x
		poly = PolynomialFeatures(degree=self.degree)
		polynominal_features = poly.fit_transform(x)
		return self.model.predict(polynominal_features)[0]


def run():
	start_date = '2014-01-01'
	end_date = '2015-12-31'

	df = pd.DataFrame(index=pd.date_range(start_date, end_date))
	my_stocks = ['AAPL', 'GOOG', 'IBM', 'CRM'];

	for stock in my_stocks:
		df = df.join(read_stock(stock), how='inner')

	df.sort_index(inplace=True)

	daily = df[1:] / df[:-1].values
	normalized = df / df.values[1]

	fig, ax1 = plt.subplots(1)
	normalized['CRM'].plot(ax = ax1)
	
	linear_space = np.arange(len(normalized.index))

	for degree in range(20):
		m = Linear_Model()
		m.train(normalized.index, normalized['CRM'], degree = degree)
		prediction_name = 'CRM_PREDICT_{}'.format(degree)
		normalized[prediction_name] = np.array( [m.predict(x) for x in linear_space])
		normalized[prediction_name].plot(ax = ax1)


	'''
	fig, (ax1, ax2, ax3,) = plt.subplots(3, sharex=True)

	df.plot(ax=ax1, title='Historical Prices')
	normalized['CRM'].plot(ax=ax1, title='CRM')


	normalized.plot(ax=ax2, title='Normalized Prices')
	daily.plot(ax=ax3, title='Daily Returns')
	'''
	plt.show()



if __name__ == '__main__':
	run()