#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL")
data = featureFormat(data_dict, features)

### your code below
n=0
for point in data:
    n=n+1
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

for d in data_dict:
    if data_dict[d]["salary"] > 1000000:
        print d
        print data_dict[d]["salary"]

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


