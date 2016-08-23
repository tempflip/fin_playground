import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn import svm, metrics



def scaledown(img):
	y_scale = 1.5
	x_scale = 1.5
	shape = img.shape
	matrix = []
	for y in range(int(shape[0] / y_scale)):
		row = []
		for x in range(int(shape[1] / x_scale)):
			subarray = img[y*y_scale : (y+1)*y_scale,  x*x_scale : (x+1)*x_scale]
			row.append(np.sum(subarray) / (16 * 2 * x_scale * y_scale))
		matrix.append(row)

	return np.array(matrix)

FILE_NAME = '_digit_rec.csv'



train_size = 4000

df = pd.read_csv(FILE_NAME)
df2 = pd.DataFrame()
df2['label'] = df['label'][:train_size]
df2['img'] = pd.Series([  np.asarray(x[1:]).reshape(28,28) for x in df.values ][:train_size])
df2['img2'] = df2['img'].apply(scaledown)
print "data processed."

#plt.imshow(df2['img2'][7], interpolation='nearest', cmap='Greys')
#plt.show()



#n = 318
#print df2['label'][n]
#plt.imshow(df2['img'][n], interpolation='nearest', cmap='Greys')
#plt.show()


target = df2['label'].values
data = [x.reshape(-1) for x in df2['img2'].values]


n = 2000
clf = svm.SVC(gamma=0.001)
clf.fit(data[:n], target[:n])

print "model created."

preds = clf.predict(data[n:])

print metrics.classification_report(target[n:], preds)




