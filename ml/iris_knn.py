from sklearn import datasets
iris = datasets.load_iris()

X = iris.data 
y = iris.target

# Generate train and test data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.5)

# Decision tree classifier
from sklearn import tree
dtclf = tree.DecisionTreeClassifier()
dtclf.fit(X_train, y_train)

dtpredictions = dtclf.predict(X_test)

# Compute accuracy 
from sklearn.metrics import accuracy_score
print accuracy_score(y_test, dtpredictions)

# K-Nearest Neighbor classifier 
from sklearn.neighbors import KNeighborsClassifier
knnclf = KNeighborsClassifier()
knnclf.fit(X_train, y_train)

knnpredictions = knnclf.predict(X_test)

# Compute accuracy
print accuracy_score(y_test, knnpredictions)