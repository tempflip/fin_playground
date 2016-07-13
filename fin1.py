import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	df = pd.read_csv("AAPL.csv")
	#print df.Close.max()
	#print df.Close.min()
	#print df.Close.mean()
	#df['vuuu'] = 'x'
	#print df.info()
	df2 = df[:50]
	print df2

	df2[['Close', 'Adj Close']].plot()

	plt.show()



if __name__ == "__main__":
	test_run()