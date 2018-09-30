# Import dependencies
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from scipy.spatial import distance

def eud(a,b):
	return distance.euclidean(a, b)

class NearestNeighborClassifier():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train

	def predict(self,X_test):
		predictions = []
		for rows in X_test:
			labels = self.closest(rows)
			predictions.append(labels)
		return predictions

	def closest(self,row):
		best_dist = eud(row, self.X_train[0])
		best_idx = 0
		for i in range(1,len(self.X_train)):
			dist = eud(row, self.X_train[i])
			if best_dist>dist:
				best_dist = dist
				best_idx = i
		return self.y_train[best_idx]

# Load datasets
iris = datasets.load_iris()

X = iris.data 
y = iris.target

# Generate train and test data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.5)

# Nearest Neighbor classifier 
nnclf = NearestNeighborClassifier()

nnclf.fit(X_train, y_train)
nnpredictions = nnclf.predict(X_test)
print y_test
print nnpredictions

# Compute accuracy
print accuracy_score(y_test, nnpredictions)