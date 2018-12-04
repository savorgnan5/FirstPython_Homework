#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import csv
csv_path = os.path.join("Resources","election_data.csv")
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    votes = 0
    candidates={}
    candidate_percentage = 0
    largest=0
    candidate_win=0
    
    Header=next(csvreader)
    for row in csvreader:
        votes = votes + 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        elif row[2] in candidates:
            candidates[row[2]]= candidates[row[2]] +1
    print("Total votes =" + str(votes))
    for key in candidates:
        candidate_percentage = candidates[key]/int(votes)
        print(f"{key}:{candidates[key]}({candidate_percentage})")
        if candidates[key] > candidate_win:
            candidate_win = candidates[key]
            win= key
print(f"The winner = {win} = {candidate_win}({candidate_percentage})")


# In[ ]:




