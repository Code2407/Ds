from sklearn import tree
print("Umang,26")

clf=tree.DecisionTreeClassifier()
#[height,hair-length,voice-pitch]

X=[[180,15,0],[167,42,1],[136,35,1],[174,15,0],[141,28,1]]
Y=['man','woman','woman','man','woman']
clf=clf.fit(X,Y)
prediction=clf.predict([[167,42,1]])
print(clf.score(X,Y))
print(prediction)
