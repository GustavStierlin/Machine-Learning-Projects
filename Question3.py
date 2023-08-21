import pandas as pd
import matplotlib.pyplot as plt

#Question 3.1
df = pd.read_csv('merka_agri_corn_experiment.csv')
X = df['corn_weight']
y = df['fertilizer_addition']
plt.scatter(X,y, color='red')

plt.title('fertilizer_addition vs corn_weight')
plt.xlabel('corn_weight')
plt.ylabel('fertilizer_addition in mg')
plt.show()

#Question 3.2
import numpy as np

def get_coeficient(x,y):
    n = np.size(x)
# mean of x and y
    m_x = np.mean(x)
    m_y =np.mean(y)

    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx= np.sum(x*x) - n*m_x*m_x

    a = SS_xy/SS_xx
    b = m_y - a*m_x

    return(a,b)

def regres_line(x,y,b):
    plt.scatter(x,y,color="red")

    y_pred= b[0]+b[1]*x

    plt.plot(x,y_pred,color="blue")
    plt.xlabel('corn weight')
    plt.ylabel('fertilizer')

    plt.show()

def main():
    df = pd.read_csv('merka_agri_corn_experiment.csv')
    y = df['corn_weight']
    X = df['fertilizer_addition']

    b= get_coeficient(X,y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    regres_line(X,y,b)

if __name__ == "__main__":
    main()
