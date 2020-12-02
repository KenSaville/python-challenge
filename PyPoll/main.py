import os
import csv
#import numpy as np
#import pandas as pd

csvpath = os.path.join('..',"PyPoll","resources", "pypoll_election_data.csv")

with open (csvpath, newline="") as csvfile:
    pollreader = csv.reader(csvfile, delimiter = ',')
    print(pollreader)

#initialize empty lists
candidates = []

# open pybank_budget file, create budget reader object

with open (csvpath, newline="") as csvfile:
    votereader = csv.reader(csvfile, delimiter = ',')
    print(votereader)

# iterate through rows, skipping first (header) row. add first candidate t list,
# then check to see if each additional candidate is in the list.  If not add it.
    i = 0
    for row in votereader:
        if i == 1:
            first_name = row[2]
            candidates.append(first_name)
        elif i > 1 and row[2] not in candidates:
                candidates.append(row[2]) 
        i += 1    

print(candidates)

# create dictionary with key:value = candidates:votes, with votes starting at 0.
votes = {}
for i in candidates:
    votes[i] = 0

print (votes)
#write analysis to file

#out_path = os.path.join("analysis", "poll_results.txt")

#with open (out_path, 'w') as newfile:

 #   newfile.write("------------------\n")
  #  newfile.write ("Election Results\n")
    
    
