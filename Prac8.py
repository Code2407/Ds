import inline as inline
import matplotlib as matplotlib
plt inline
import inline
import matplotlib
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
print("Umang,26")

df=pd.read_csv('mangoprice_1.csv')
print(df)

# %matplotlib inline
plt.xlabel('year')
plt.ylabel('mangoes_price')
plt.scatter(df.year,df.mango_price,color='blue',marker='.',linewidth='5')

new_df=df.drop('mango_price',axis=1)
#print(new_df)

mango_price=df.mango_price
#print(mango_price)

reg_model=linear_model.LinearRegression()
reg_model.fit(new_df,mango_price)

#Predict the price of mango in the year 2020, 2021
a=reg_model.predict([[2020]])
b=reg_model.predict([[2021]])

print(a)
print(b)

#y=mx+c
#=2020*5.6+(-11353.33)

print(reg_model.coef_)
print(reg_model.intercept_)
print(reg_model.score(new_df,mango_price))

year_df=pd.read_csv('years.csv')
print(year_df)

price=reg_model.predict(year_df)
print(price)

year_df['mango_price']=price
print(year_df)

year_df.to_csv("priceprediction.csv")
plt.show()
