#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.draw()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score
from time import time

# k-nearest neighbours, classic, simple, easy to understand
# sklearn.ensamble.AdaBoostClassifier. adaboost, ensamble methods
# random forest, ensamble methods
###
# 1. Do some research.
# 2. Find sklearn documentation.
# 3. Deploy it!
# 4. Use it to make predictions.
# 5. Evaluate it using accuracy_score.
###
print "Evaluating using AdaBoost"

### Create the classifier with the chosen algorithm.
clf = AdaBoostClassifier(n_estimators=100, learning_rate=1.0)

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

try:
    prettyPicture(clf, features_test, labels_test)
    plt.show()
except NameError:
    pass
