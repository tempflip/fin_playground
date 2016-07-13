import pandas as pd 
import numpy as np 
import scipy.optimize as spo
import matplotlib.pyplot as plt


def f(x):
	y = (x - 1.5)**2 + (x + 20) + 0.5
	#print 'X = {}, Y = {}'.format(x, y)
	return y

def line_data(space, coeff):
	return space * coeff[0] + coeff[1]

def data_diff_norm_sum(data1, data2):
	return sum(abs(data1 - data2)**2)

def error(line_guess, space, points_data):
	return data_diff_norm_sum(points_data, line_data(space, line_guess))

def run():
	line = np.float32([2,3])
	x_orig = np.linspace(0, 9, 10)
	

	y_orig = line_data(x_orig, line)  #####x_orig * line[0] + line[1]


	noise_sigma = 3
	noise = np.random.normal(0, noise_sigma, y_orig.shape)

	#print noise

	data = y_orig + noise

	print y_orig

	print data

	print data_diff_norm_sum(y_orig, data)

	line_guess = (10,10)

	minimized_error = spo.minimize(error, line_guess, method="SLSQP", args=(x_orig, data) )

	print minimized_error

	fitted_line1 = (minimized_error.x[0], minimized_error.fun)
	fitted_line2 = (minimized_error.x[1], minimized_error.fun)

	print fitted_line1

	plt.plot(x_orig, y_orig, 'b--', label = 'original line')
	plt.plot(x_orig, line_data(x_orig, line_guess), 'r--')
	plt.plot(x_orig, line_data(x_orig, fitted_line1), 'o')
	plt.plot(x_orig, line_data(x_orig, fitted_line2), '+')

	plt.plot(x_orig, data, '*')
	plt.show()



	
	#xplot = np.linspace(-5, 5, 200)
	#yplot = f(xplot)

	#plt.plot(xplot, yplot)
	#plt.plot(min_result.x, min_result.fun, 'ro')

	#plt.show()

if __name__ == '__main__':
	run()
