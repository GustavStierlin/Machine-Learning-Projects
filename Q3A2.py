import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


df = pd.read_csv('real_estate_data.csv')

x_plot = df[['fertilizer_addition']]
y_plot = df[['corn_weight']]

plt.scatter (x_plot,y_plot, color = 'blue')
plt.xlabel('fertilizer_addition')
# naming the y axis
plt.ylabel('corn_weight')

# giving a title to my graph
plt.title('Fertilizer Addition vs Corn Addition')

# function to show the plot
plt.show()

#Question 3.2
X = np.array(df['fertilizer_addition']).reshape(-1,1)
y = np.array(df['corn_weight']).reshape(-1,1)

from sklearn.model_selection import train_test_split
df.dropna(inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.99)


from sklearn.linear_model import LinearRegression
rlm = LinearRegression()
rlm.fit(X_train,y_train)

print(rlm.score(X_train,y_train))

y_pred = rlm.predict(X_train)

plt.scatter (X_train,y_pred, color = 'green')
plt.xlabel ('fertilizer addition')
plt.ylabel ('corn weight in mg')
plt.title ('Regressed Data of Fertillizer Addition vs Corn Weight')
plt.show()

c = rlm.intercept_
m= rlm.coef_
print("The final equation is: Weight=" ,m,"*fertilizer_addition+",c)

import pylab
pylab.scatter(x_plot,y_plot,color="blue",s=10)
pylab.scatter(X_train,y_pred,color="black",s=10)
pylab.ylabel('corn weight')
pylab.xlabel('fertilizer addition in mg')
pylab.title('Fertilizer Addition against Corn Addition superimposed scatterplot')
pylab.legend(["Scattered Data","Regressed Scatterplot"])
pylab.show()

Final_weight = (m*50+c)
print("The expected wight of the corn should be: ",Final_weight," mg")