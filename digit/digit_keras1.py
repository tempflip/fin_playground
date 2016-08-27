from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
import pandas as pd
import numpy as np

'''

plt.subplot(221)
plt.imshow(X_train[0], cmap=plt.get_cmap('gray'))
plt.subplot(222)
plt.imshow(X_train[1], cmap=plt.get_cmap('gray'))
plt.subplot(223)
plt.imshow(X_train[2], cmap=plt.get_cmap('gray'))
plt.subplot(224)
plt.imshow(X_train[3], cmap=plt.get_cmap('gray'))
# show the plot
plt.show()
'''



# define baseline model
def baseline_model():
	# create model
	model = Sequential()
	model.add(Dense(num_pixels, input_dim=num_pixels, init='normal', activation='relu'))
	model.add(Dense(num_classes, init='normal', activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model



FILE_NAME = '_digit_rec.csv'

set_size = 4000
train_size = 2000

df = pd.read_csv(FILE_NAME)

labels =  df.values[:,0:1]
data = df.values[:, 1:]


'''df2 = pd.DataFrame()
df2['label'] = df['label'][:set_size]
df2['img'] = pd.Series(np.asarray(df.values[1:])[:set_size])
df2['img'] = df2['img'] / 256
'''



num_pixels = 28 * 28

X_train = data[:train_size] / 256
y_train = labels[:train_size]

X_test = data[train_size:] / 256
y_test = labels[train_size:]

#X_train = df2['img'][:train_size].values
#y_train = df2['label'][:train_size].values

#X_test = df2['img'][train_size:].values
#y_test = df2['label'][train_size:].values




y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]


print 'x train shape ', X_train.shape
print 'y train shape ', y_train.shape

print 'x test shape ', X_test.shape
print 'y test shape', y_test.shape


model = baseline_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), nb_epoch=10, batch_size=200, verbose=2)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))
