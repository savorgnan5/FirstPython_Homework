#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
csv_path = os.path.join("Resources","Payback.csv")
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    average=0
    Sum=0
    row=0
    largest=0
    smallest=0
    Number_ofmonths=0
    Profit_loss=0
    Header= next(csvreader)

    for row in csvreader:
        Number_ofmonths = Number_ofmonths +1
        Profit_loss = int(row[1]) + Profit_loss
        if float(row[1]) >largest: 
                largest = int(row[1])
        elif float(row[1]) <smallest:
             smallest = int(row[1])
                
    Average_Pro_lost = Profit_loss/Number_ofmonths
    
print(f"Number of months= {Number_ofmonths}")
print(f"Profit/Loss= {Profit_loss}")
print(f"The average profit/loss = {Average_Pro_lost}")
print(f"The largest profit = {largest}")
print(f"The smallest profit = {smallest}")


# In[ ]:




