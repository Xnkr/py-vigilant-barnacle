# Import packages 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sys # system processes

# keeps the plots in one place. calls image as static pngs
import matplotlib.pyplot as plt # side-stepping mpl backend
import matplotlib.gridspec as gridspec # subplots
import mpld3 as mpl # web plots

# Import models from scikit learn module:
from sklearn.model_selection import train_test_split,KFold # models
#from sklearn.cross_validation import KFold   # For K-fold cross validation

from sklearn.linear_model import LogisticRegression # LogisticRegression
from sklearn.ensemble import RandomForestClassifier # RandomForest
from sklearn.neighbors import KNeighborsClassifier # KNN
from sklearn.ensemble import AdaBoostClassifier # AdaBoost
from sklearn.naive_bayes import GaussianNB # NaiveBayes
from sklearn.tree import DecisionTreeClassifier, export_graphviz # Decision Tree
from sklearn.svm import SVC,LinearSVC # SVM
from sklearn.neural_network import MLPClassifier # Neural net

from sklearn.externals.six import StringIO
import pydot_ng as pydot

from sklearn import metrics # Metrics for accuracy

def classification_model(model, data, predictors, outcome):
	#Fit the model:
	model.fit(data[predictors],data[outcome])
	  
	#Make predictions on training set:
	predictions = model.predict(data[predictors])
	  
	#Print accuracy
	accuracy = metrics.accuracy_score(predictions,data[outcome])
	print("Accuracy : %s" % "{0:.3%}".format(accuracy))
	
	#Perform k-fold cross-validation with 5 folds
	kf = KFold(n_splits=5)
	error = []
	for train, test in kf.split(data):
		# Filter training data
		train_predictors = (data[predictors].iloc[train,:])
		
		# The target we're using to train the algorithm.
		train_target = data[outcome].iloc[train]
		
		# Training the algorithm using the predictors and target.
		model.fit(train_predictors, train_target)
		
		#Record error from each cross-validation run
		error.append(model.score(data[predictors].iloc[test,:], data[outcome].iloc[test]))
		
		print("Cross-Validation Score : %s" % "{0:.3%}".format(np.mean(error)))
		
	#Fit the model again so that it can be refered outside the function:
	model.fit(data[predictors],data[outcome]) 

def get_prediction(prediction):
	prediction = prediction.tolist()
	for i,item in enumerate(prediction):
		if item == 1:
			prediction[i] = "Stage 1"
		elif item == 2:
			prediction[i] = "Stage 2"
		else:
			prediction[i] = "Stage 3"
	print prediction

def DT_Classify(predictor_var, outcome_var, traindf, Ptest_X):
	# Decision Tree	
	model = DecisionTreeClassifier(random_state=22)
	classification_model(model,traindf,predictor_var,outcome_var)
	dot_data = StringIO()
	features_mean=list(traindf.columns[0:3])
	print features_mean
	export_graphviz(model,
						feature_names = features_mean,
						filled = True, rounded = True,
						out_file = dot_data) 
	# classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
	graph.write_pdf("lndc.pdf")
	get_prediction(prediction)
	
def KNN_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	model = KNeighborsClassifier()
	classification_model(model,traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)

def RF_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	# Random Forest
	model = RandomForestClassifier(n_estimators=100,random_state=22)
	classification_model(model, traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)
	
def AdaBoost_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	model = AdaBoostClassifier(random_state=22)
	classification_model(model,traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)
		
def LR_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	# Logistic Regression
	model=LogisticRegression(random_state=22)
	classification_model(model,traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)

def SVM_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	model = LinearSVC(random_state=22)
	classification_model(model,traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)
	
def NB_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	model = GaussianNB()
	classification_model(model,traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)
	
def NN_Classify(predictor_var, outcome_var, traindf, testdf, Ptest_X):
	model = MLPClassifier(hidden_layer_sizes=(200,),solver = 'lbfgs', max_iter=200, random_state=22)
	classification_model(model,traindf,predictor_var,outcome_var)
	classification_model(model,testdf,predictor_var,outcome_var)
	prediction = model.predict(Ptest_X)
	# featimp = pd.Series(model.feature_importances_, index=predictor_var).sort_values(ascending=False)
	# print(featimp)
	get_prediction(prediction)
	
if __name__ == '__main__':
	x = float(sys.argv[1])
	df = pd.read_csv("TRAINING.csv",header = 0)
	df['Label'] = df['Label'].map({'Stage 1':1,'Stage 2':2, 'Stage 3':3})
	# Histogram of Training data
	plt.hist(df['Label'])
	plt.title('Stage (1 , 2, 3)')
	plt.draw()

	features_mean=list(df.columns[0:3])
	df1=df[df['Label'] ==1]
	df2=df[df['Label'] ==2]
	df3=df[df['Label'] ==3]

	# Parameter Bar graph
	plt.rcParams.update({'font.size': 8})
	fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10,10))
	axes = axes.ravel()
	for idx,ax in enumerate(axes):
		ax.figure
		binwidth= (max(df[features_mean[idx]]) - min(df[features_mean[idx]]))/50
		ax.hist([df1[features_mean[idx]],df2[features_mean[idx]],df3[features_mean[idx]]], bins=np.arange(min(df[features_mean[idx]]), max(df[features_mean[idx]]) + binwidth, binwidth) , alpha=0.5,stacked=True, normed = True, label=['1','2','3'],color=['r','g','b'])
		ax.legend(loc='upper right')
		ax.set_title(features_mean[idx])

	plt.tight_layout()
	plt.draw()

	#Parameter Scatter plot
	observables = df.loc[:,features_mean]
	color_wheel = {3: "blue", 1: "red", 2: "green"}
	colors = df["Label"].map(lambda x: color_wheel.get(x))
	pd.scatter_matrix(observables, c=colors, alpha = 0.5, figsize = (15, 15), diagonal = 'kde');

	#traindf, testdf = train_test_split(df, test_size = 0.3)
	dfP = pd.read_csv('parameter.csv',sep = ',', header=0)
	Ptest_X = dfP.loc[:,['Area','Perimeter','Radius']].as_matrix()

	classifiers = {1 : DT_Classify,
           2 : KNN_Classify,
           3 : RF_Classify,
           4 : AdaBoost_Classify,
           5 : LR_Classify,
           6 : SVM_Classify,
           7 : NB_Classify,
           8 : NN_Classify,
	}

	classifiers[x](features_mean, 'Label', df, Ptest_X)
	# plt.show()
	
	# #Random forest
	# predictor_var = features_mean
	# outcome_var='Label'





