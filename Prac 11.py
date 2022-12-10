import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
print("Umang,26")

df=pd.read_csv('onionprice.csv')
print(df)

#%matplotlib inline
plt.xlabel('year')
plt.ylabel('onions_price')
plt.scatter(df.year,df.onion_price,color='blue',marker='.',linewidth='5')

new_df=df.drop('onion_price',axis=1)
#print(new_df)

onion_price=df.onion_price
#print(onion_price)

reg_model=linear_model.LinearRegression()
reg_model.fit(new_df,onion_price)

#Predict the price of onion the year 2020, 2021
a=reg_model.predict([[2020]])
b=reg_model.predict([[2021]])

print(a)
print(b)

#y=mx+c
#=2020*5.6+(-11353.33)

print(reg_model.coef_)
print(reg_model.intercept_)
print(reg_model.score(new_df,onion_price))

year_df=pd.read_csv('years.csv')
print(year_df)

price=reg_model.predict(year_df)
print(price)

year_df['onion_price']=price
print(year_df)

year_df.to_csv("priceprediction.csv")
