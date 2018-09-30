from sklearn import tree

features = [[150,0],[160,0],[190,1],[186,1]]
labels = ['apple','apple','orange','orange']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print clf.predict([[170,0]])
print clf.score([[170,0]],['orange'])