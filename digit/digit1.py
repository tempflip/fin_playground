import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()

images =  digits.images
target = digits.target


assert(len(images) == len(target))



sample_n = len(images)

data = images.reshape(sample_n, -1)



clf = svm.SVC(gamma=0.001)
clf.fit(data[:sample_n / 2], target[:sample_n / 2])




expected = target[sample_n / 2:]
predicted = clf.predict(data[sample_n / 2:])

print metrics.classification_report(expected, predicted)

print metrics.confusion_matrix(expected, predicted)


print [x for x in zip(expected, predicted) if x[0] != x[1]]


plt.imshow(images[100], interpolation = 'nearest', cmap='Greys')
plt.show()
