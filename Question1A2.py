import mysql.connector
from mysql.connector import Error
import sklearn
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
import tensorflow as tf
from tensorflow import keras



#Question 1.1 Connect the database
#Try to connect to DB on my local system
try:
    conn = mysql.connector.connect ( host='localhost',database= 'poer_bank_creditdb',user = 'root',
                                   password = '__Gustav16__')                                  
    if conn.is_connected():  #If connected get the information of the server and output
        db_info = conn.get_server_info()
        print("Connected to server", db_info)
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Youre connected",record)

except Error as e:   #if not connected display an error message
    print("error connecting to mysql",e)

query3 = "Select cust_details.age, cust_details.gender, cust_details.marital_status, cust_details.nqf_level, loan_records.loan_amount, loan_records.payback_term  from cust_details inner join loan_records on cust_details.id = loan_records.id"
df = pd.read_sql(query3, conn)   #Query the dataframe
df3 = df

df3["marital_status"].replace(['married', 'single', 'divorced'], [1,-1,0], inplace=True)  #Replace marital status with numbers

#Normalize the features

df3["marital_status"]= df3["marital_status"]/df3["marital_status"].max()   
df3["age"]= df3["age"]/df3["age"].max()
df3["nqf_level"]= df3["nqf_level"]/df3["nqf_level"].max()

Final_df = df3.drop(columns=["gender"])    #drop the gender column from the dataframe

X = Final_df.drop(columns=["payback_term"])   #drop payback term column from x
y = Final_df["payback_term"]                 #y is only the payback term

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

SC_x = StandardScaler()
xTrain_scale = SC_x.fit_transform(X_train)
xTest_scaled = SC_x.fit_transform(X_test)


mlp = MLPRegressor(hidden_layer_sizes=(100,100),activation='relu',solver='adam',max_iter=1000).fit(xTrain_scale,y_train)   

y_pred2 = mlp.predict(xTest_scaled)
print("The Score with Tested:",(r2_score(y_pred2,y_test))) #Print the accuracy score 

y_pred = mlp.predict(xTrain_scale)
print("The Score with trained:",(r2_score(y_pred,y_train)))


x_plt = [y_train]
y_plot = [y_pred]
plt.scatter(x_plt,y_plot, color='red')

plt.title('Training data vs Model prediction')
plt.xlabel('Training data')
plt.ylabel('Model prediction')
plt.show()

x_plot2 = [y_test]
y_plot2 = [y_pred2]
plt.scatter(x_plot2,y_plot2, color ='blue')
plt.title('Test data vs Model prediction')
plt.xlabel('Test data')
plt.ylabel('Predicted data')
plt.show()


#Question 1.3
new_dataDF = pd.read_csv('Bankdata.csv')
New_FinalDF = new_dataDF.drop(columns=["gender"])
New_FinalDF["marital_status"].replace(['married', 'single', 'divorced'], [1,-1,0], inplace=True)
newX = New_FinalDF[['age','marital_status','nqf_level','loan_amount']]



newX["marital_status"]= newX["marital_status"]/newX["marital_status"].max()   
newX["age"]= newX["age"]/newX["age"].max()
newX["nqf_level"]= newX["nqf_level"]/newX["nqf_level"].max()

newX_scale = SC_x.fit_transform(newX)

new_pred = mlp.predict(newX_scale)
print("Loan payback term:",new_pred)
print("lenght",len(newX))