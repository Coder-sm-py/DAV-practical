import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

z = X * y
X2 = X * X

a = ((len(X) * sum(2)) - (sum(X) * sum(y))) / ((len(X) * sum(X2)) - (sum(X) * sum(X)))
b = (sum(y) - (a * sum(X))) / (len(X))

x_test = [1.7 , 2.3 , 3.9 , 4.5 , 5.4]
y_pred = []
for i in range (len(x_test)):
    y_pred.append((a * x_test[i]) + b)

from sklearn.linear_model import LinearRegression
regresoor = LinearRegression()
regresoor.fit(X.reshape(-1,1),y)

plt.plot(X.reshape(-1,1), regresoor.predict(X.reshape(-1,1)), color = 'blue', label = 'Best fit line')
plt.scatter(X,y,color = 'green',label = 'Actual points')
plt.scatter(x_test,y_pred, color = 'red',label = 'Predicted points')
plt.title('Salary vs Experience')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.legend(loc = 'upper left')
plt.show()