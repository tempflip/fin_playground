import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_csv('HairEyeColor.csv')



print df.columns

#df2 = df[df.Sex == 'Male']

t1 = time.time()

df2 = df.loc[:,['Eye','Hair','Freq']]
df2 = df2.groupby(['Eye', 'Hair']).sum()

t2 = time.time()

print df2

print "took {} seconds".format(t2-t1)





