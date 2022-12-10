from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
print("Umang,26")

colname=['sepal-lenght','sepal-width','petal-length','petal-width','Class']
iris_data=pd.read_csv('iris.data',names=colname)
#Frequency distribution of Class
iris_outcome=pd.crosstab(index=iris_data['Class'],columns='count')

#print(iris_outcome)

iris_setosa=iris_data.loc[iris_data['Class']=="Iris-setosa"]
iris_veriscolor=iris_data.loc[iris_data['Class']=="Iris-veriscolor"]
iris_verginica=iris_data.loc[iris_data['Class']=="Iris-virginca"]

iris_data['Class']=pd.Categorical(iris_data["Class"])
iris_data['Class']=iris_data["Class"].cat.codes

X=iris_data.values[:,0:4]
y=iris_data.values[:,4]

#Number of Cluster
kmeans=KMeans(n_clusters=3)

#Fitting the input data
kmeans=kmeans.fit(X)

#Getting the cluster label
labels=kmeans.predict(X)

#Centroid value
centroids=kmeans.cluster_centers_

from sklearn.metrics import classification_report

target_names=['Iris-setosa','Iris-veriscolor','Iris-virginca']
print(classification_report(iris_data['Class'],kmeans.labels_,target_names=target_names))
