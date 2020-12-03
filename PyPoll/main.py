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

#print(candidates)

# create dictionary with key:value = candidates:votes, with votes starting at 0.
votes = {}
for i in candidates:
    votes[i] = 0
#print (votes)

#loop through file again, adding 1 to values when row[2] matches key.  
# Could probably just made dictionary in first loop

with open (csvpath, newline="") as csvfile:
    votereader = csv.reader(csvfile, delimiter = ',')
    print(votereader)

# iterate through rows, skipping first (header) row. add first candidate t list,
# then check to see if each additional candidate is in the list.  If not add it.
    i = 1
    for row in votereader:
        if i > 1:
            votes[row[2]] +=1
        i += 1

#print(votes)

# the above worked.  Creating a dictionary with name:vote total

first_total = votes[candidates[0]]
for name in candidates:
    if votes[name] > first_total:
        winner = name
    else:
        winner = candidates[0]
#print(winner)

vote_total = 0
for name in votes:
    vote_total = vote_total + votes[name]

#print("vote total = " + str(vote_total))

#calculate percents
percents = {}
for name in candidates:
    percents[name] = round((votes[name]/vote_total* 100),2)
#print(percents)

# make a new dictionaty that has the name as key and the vote_total and percent as a list.
#   to make it easier to accesss
combined = {}
for name in candidates:
    combined[name] = [votes[name], percents[name]]

#print (combined['Khan'][1])

# print results to screen

print ("\n\nElection Results:")
print ("----------------------")
print ("Total votes: " + str(vote_total))
print ("----------------------")
print("Candidate"+ "\t" + "raw votes" + "\t" + "percent".expandtabs(30)) 
print ("__________________________________")
for name in candidates:
    print(name + "\t" + str(combined[name][0])+ "\t" + str(combined[name][1])

print("\nAND THE WINNER IS ...\n\n" + winner)

print("\nWho knew his wrath would pay off so well ?\n")


#write analysis to file

out_path = os.path.join("analysis", "poll_results.txt")

with open (out_path, 'w') as newfile:

    newfile.write ("\n\nElection Results:\n")
    newfile.write ("----------------------")
    newfile.write ("\n\nTotal votes: " + str(vote_total))
    newfile.write ("\n----------------------")
    newfile.write ("\nCandidate" + "\t" + "raw votes" + "\t" + "percent".expandtabs(30)) 
    newfile.write ("\n\n")
    for name in candidates:
        newfile.write(name + "\t" + str(combined[name][0])+ "\t" + str(combined[name][1]) + "\n".expandtabs(30))

    newfile.write ("\nAND THE WINNER IS ...\n\n" + winner)

    newfile.write ("\n\nWho knew his wrath would pay off so well ?\n")



    
    
