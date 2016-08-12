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
import itertools

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
        my_space = np.array(training_x_matrix)
        my_space = my_space.reshape(-1,len(my_space))

        poly = PolynomialFeatures(degree=self.degree)
        # polynominal features of the space
        my_space_features = poly.fit_transform(my_space) 

        # training the model
        regr = linear_model.Ø()
        regr.fit(my_space_features, training_y_matrix)
        self.model = regr

        #print my_space_features
        self.description = "i'm a linear model of {} degree".format(self.degree)
        # calculating the MSE with the training data
        self.mse = mean_squared_error(training_y_matrix, [self.predict(x) for x in my_space])
    

    def predict(self, x):
        ## as it is trained on polynominal features, we need to transform x
        poly = PolynomialFeatures(degree=self.degree)
        polynominal_features = poly.fit_transform(x)[0]

        print polynominal_features.reshape
        return self.model.predict(polynominal_features)



# loading


boston = load_boston()
df = pd.DataFrame(boston.data, columns = boston.feature_names)
df['MEDV'] = boston.target

# normalizing the dataframe
norm = (df - df.min())
norm = norm / norm.max()


degree_set = [1,2,3,4]

'''
mse_df = pd.DataFrame(columns = norm.columns)
for col in norm.columns.values:
    s = []
    for degree in degree_set:
        model = Linear_Model()
        model.train([norm[col]], norm['MEDV'], degree = degree)
        s.append(model.mse)
        print col, model, model.mse
    mse_df[col] = s

print mse_df
'''

#metrics = ['B', 'MEDV', 'TAX', 'LSTAT']
metrics = norm.columns.values

mse_dict = {}

for i in range(3):
    metrics_list = list(itertools.combinations(metrics, i+1))
    for mtr in metrics_list:
        for degree in degree_set:
            model = Linear_Model()
            model.train([norm[m] for m in mtr], norm['MEDV'], degree = degree)
            mse_dict['-'.join(mtr) + str(degree)] = model


sorted_models = sorted(mse_dict.iteritems(), key = lambda model : model[1].mse)

for (name, model) in sorted_models:
    print name, model.mse




'''
n = [ model.predict( [norm.iloc[i]['TAX'], norm.iloc[i]['B']] )[0] for i in norm.index.values]
norm['PRE-TAX-B'] = n

model2 = Linear_Model()
model.train([norm['TAX']], norm['MEDV'], degree = 2)
norm['PRE-TAX'] = [ model.predict( x )[0] for x in norm['TAX'].values]

model3 = Linear_Model()
model.train([norm['CRIM']], norm['MEDV'], degree = 1)
norm['CRIM-B'] = [ model.predict( x )[0] for x in norm['CRIM'].values]
'''


'''






ax = norm.plot(kind='scatter', x = 'CRIM', y = 'MEDV')
norm.plot(kind='scatter', x = 'CRIM-B', y = 'MEDV', ax = ax)


plt.show()
print norm
'''


'''

'''

