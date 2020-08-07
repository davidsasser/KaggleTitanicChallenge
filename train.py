from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump

data_path = 'data/titanic_train.csv'
with open(data_path, 'r') as f:
    dataset = np.loadtxt(f, delimiter=",")

x_train = dataset[:,0:5]
y_train = dataset[:,6]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)


dump(clf, 'model/classifier.joblib') 