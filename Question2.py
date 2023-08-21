import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
#Question 2.1
df = pd.read_csv('Prek_HR_data.csv')
X = df[['nqf','age','exp_level']]
y = df[['q_score']]
feature_cols = ['nqf','age','exp_level']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.15)
#Question 2.2
clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
y_prediction2 = clf.predict(X_train)

print("Accuracy for test:",metrics.accuracy_score(y_test,y_pred))
print("Accuracy for training:",metrics.accuracy_score(y_train,y_prediction2))

from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
import six
import sys
sys.modules['sklearn.externals.six'] = six
from six import StringIO
import os


dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names= feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Mygrafiek.bmp')
Image(graph.create_png())