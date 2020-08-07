import sklearn
import numpy as np
from joblib import load
import csv

clf = load('model/classifier.joblib')

data_path = 'data/titanic_test.csv'
with open(data_path, 'r') as f:
    dataset = np.loadtxt(f, delimiter=",")

x_test = dataset[:,0:5]

y_test = clf.predict(x_test)

wtr = csv.writer(open ('submission.csv', 'w'), delimiter=',', lineterminator='\n')

for i in range(0,418):
    ans = [None] * 2
    if(i == 0):
        wtr.writerow(['PassengerId', 'Survived'])
    
    ans[0] = int(x_test[i][0])
    ans[1] = int(y_test[i])

    wtr.writerow(ans)
    