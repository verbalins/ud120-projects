#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import os
fileDir = os.getcwd()
enron_data = pickle.load(open(os.path.join(fileDir, 'final_project\\final_project_dataset.pkl'), "r"))

## Number of persons
print "Number of persons: ", len(enron_data)

## Number of features.
print "Number of features: ", len(enron_data['PRENTICE JAMES'])

## Number of POIs.
# poi = 10 When adding the extra data.
poi = 0
salary = 0
known_email = 0
total_payments_NaN = 0
total_payments = 0
# total_payments_poi = 10 When adding the extra data.
total_payments_poi = 0
for x in enron_data:
    if enron_data[x]["poi"]:
        poi += 1.0
        if enron_data[x]["total_payments"] == 'NaN':
            total_payments_poi += 1.0

    if enron_data[x]["salary"] != 'NaN':
        salary += 1

    if enron_data[x]["email_address"] != 'NaN':
        known_email += 1

    if enron_data[x]["total_payments"] == 'NaN':
        total_payments_NaN += 1.0
    else:
        total_payments += 1.0

print "Number of POIs: ", poi
print "Number of quantified salaries: ", salary
print "Known email adresses: ", known_email

print "Total payments not known, percentage of total dataset: ", total_payments_NaN/(total_payments+total_payments_NaN)
print "Total payments not known, percentage of POIs: ", total_payments_poi/poi

print "James Prentice stock value: ", enron_data['PRENTICE JAMES']['total_stock_value']

print "Number of emails from Wesley Colwell to POIs: ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print "Value of stock options by Jeff Skilling ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "Total payments for Kenneth Lay: ", enron_data['LAY KENNETH L']['total_payments']
print "Total payments for Jeffrey Skilling: ", enron_data['SKILLING JEFFREY K']['total_payments']
print "Total payments for Andrew Fastow: ", enron_data['FASTOW ANDREW S']['total_payments']