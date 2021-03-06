'''
    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over 
                 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds 
                 river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks 
                 by town
    13. LSTAT    % lower status of the population
    14. MEDV     Median value of owner-occupied homes in $1000's
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

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

class Compined_Linear_Models(Model):
    def __init__(self):
        Model.__init__(self)
        self.model_list = []

    def addModel(self, model):
        self.model_list.append(model)

    def predict(self, x):
        p = 0
        for model in self.model_list:
            p += model.predict(x)
        return p / len(self.model_list)

# loading
boston = load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['MEDV'] = boston.target


# normalizing the dataframe
norm = (df - df.min())
norm = norm / norm.max()

#training and predict
#cols = ['CRIM', 'B', 'LSTAT', 'DIS']
cols = ['CRIM']

predictions = pd.DataFrame()
combined = Compined_Linear_Models()

for col in cols:
    regr = Linear_Model()
    regr.train(norm[col], norm['MEDV'], degree=5)
    combined.addModel(regr)
    predictions[col] = [regr.predict(x) for x in norm[col].values]
    print "MSE for {}: {}".format(col, mean_squared_error(norm['MEDV'], predictions[col]))

predictions['COMB'] = [combined.predict(x) for x in norm['B'].values]

print "MSE for COMP: {}".format(mean_squared_error(norm['MEDV'], predictions['COMB']))


#print mean_squared_error(norm['MEDV'], predict)

#plot
ax = None
for col in cols:
    ax = norm.plot(kind='scatter', x = col, y='MEDV', ax = ax)
    plt.plot(norm[col], predictions[col].values, '.')
    #plt.plot(norm['B'], predictions['COMB'].values, 'go')

plt.show()