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
		my_space = training_x_matrix.reshape(-1,1)
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


class Linear_Model_Avg(Linear_Model):
	def __init__(self):
		Linear_Model.__init__(self)

	def predict(self, x):
		poly = PolynomialFeatures(degree=self.degree)
		polynominal_features = poly.fit_transform(x)
		return self.model.predict(polynominal_features).flatten().mean()

def run():
	start_date = '2014-12-01'
	end_date = '2015-01-10'

	df = pd.DataFrame(index=pd.date_range(start_date, end_date))
	my_stocks = ['AAPL', 'GOOG', 'IBM', 'CRM'];

	for stock in my_stocks:
		df = df.join(read_stock(stock), how='inner')

	df.sort_index(inplace=True)

	#daily = df[1:] / df[:-1].values
	normalized = df / df.values[1]

	train_y = normalized[['AAPL', 'GOOG']]['2014-12-01':'2014-12-31']
	train_space = np.arange(len(train_y.index))
	full_space = np.arange(len(normalized.index))

	m = Linear_Model_Avg()
	m.train(train_space, train_y.values, degree = 20)

	normalized['PRE'] = [m.predict(x) for x in full_space]	


	fig, ax1 = plt.subplots(1)


	normalized['AAPL'].plot(ax = ax1)
	normalized['GOOG'].plot(ax = ax1)
	normalized['CRM'].plot(ax = ax1)
	#normalized['PRE'].plot(ax = ax1)
	
	#plt.plot(normalized['PRE'], 'o')
	plt.axvline(x = '2014-12-31')
	


	plt.show()



if __name__ == '__main__':
	run()