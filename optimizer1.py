import pandas as pd 
import numpy as np 
import scipy.optimize as spo
import matplotlib.pyplot as plt


def f(x):
	y = (x - 1.5)**2 + (x + 20) + 0.5
	#print 'X = {}, Y = {}'.format(x, y)
	return y

def run():
	x_guess = 5
	min_result = spo.minimize(f, x_guess, method = 'SLSQP', options = {'disp' : True})

	print min_result

	print f(min_result.x)

	
	xplot = np.linspace(-5, 5, 200)
	yplot = f(xplot)

	plt.plot(xplot, yplot)
	plt.plot(min_result.x, min_result.fun, 'ro')

	plt.show()

if __name__ == '__main__':
	run()
