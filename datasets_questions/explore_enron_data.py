#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("Hello world")

c=0
n=0
for e in enron_data.keys():
   if enron_data[e]["poi"]:
       c=c+1
       print enron_data[e]["total_payments"]
       if math.isnan(float(enron_data[e]["total_payments"])):
           n=n+1
           
       
print n
print c


