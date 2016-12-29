#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

print "Classifying with SVM"

### Create classifier
clf = SVC(C=10000.0, kernel="rbf")

### Slice the training data down to 1%.
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]

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
print "Element 10: ", pred[10]
print "Element 26: ", pred[26]
print "Element 50: ", pred[50]
nrChris = pred.sum()
print "Number of predicted mails written by Chris: ", nrChris
print "Number of predicted mails written by Sara: ", len(pred)-nrChris
#########################################################