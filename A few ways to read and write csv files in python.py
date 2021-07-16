# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:26:15 2021

@author: abc
"""

import csv

#read the csv file
with open('fruits1.csv') as myFile:
    reader = csv.reader(myFile)
    for row in reader:
        print(row)
        
        
import pandas as pd    #To read data or analysis the data we use pandas library

data = pd.read_csv('fruits1.csv')
print(data.head(10))



#Write the csv file

#method 1
import csv
some_list=[['apples','oranges','grapes','mangoes'],[20,25,42,35]]

with open('fruits4.csv','w',newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter = ",")
    for fruit in some_list:
        writer.writerow(fruit)
        
#method 2

import csv

some_list = [['apples','oranges','grapes','mangoes'],[20,25,42,35]]
output_file = open('fruits5.csv','w')
with output_file:
    writer = csv.writer(output_file)
    writer.writerow(some_list)




#method 2

import csv
header = ['name','age','ZIP']
rows = [['John',30,94568],
        ['varshil',40,94588],
        ['Mary',50,94566]]

with open('people.csv','w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    for row in rows:
        csv_writer.writerow(row)


#method 3

import csv

header = ['name','age','ZIP']
rows = [{'name' : 'John','age':30,'ZIP' : 94568},
        {'name' : 'Varshil','age':40,'ZIP' : 94589},
        {'name' : 'Big Show','age':50,'ZIP' : 94566}]

with open('people1.csv','w') as file:
    csv_writer = csv.DictWriter(file, fieldnames=header)
    csv_writer.writeheader()           #write header
    csv_writer.writerows(rows)












