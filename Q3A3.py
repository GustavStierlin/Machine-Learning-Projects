import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('merka_agri_corn_experiment.csv')
#X = df[['fertilizer_addition']]
#Y = df[['corn_weight']]
FinalDF = df['fertilizer_addition','corn_weight']
FinalDF.columns=['fertilizer_addition','corn_weight']
sns.lmplot(x="fertilizer_addition",y="corn_weight",data=FinalDF,ci=None)