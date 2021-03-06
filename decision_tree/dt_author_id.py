#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("/tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score

print "Classifying with DecisionTree"

### Create classifier with min samples split 40.
clf = tree.DecisionTreeClassifier(min_samples_split=40)

### Fit the training data.
t0 = time()
clf.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

### Predict on the test data.
t0 = time()
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t0, 3), "s"

### Print accuracy.
print accuracy_score(labels_test, pred)
nrChris = pred.sum()
print "Number of predicted mails written by Chris: ", nrChris
print "Number of predicted mails written by Sara: ", len(pred)-nrChris
print "Number of features in the data: ", len(features_train[0])
#########################################################


