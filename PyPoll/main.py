import os
import csv
import numpy as np
import pandas as pd

csvpath = os.path.join('..',"PyPoll","resources", "pypoll_election_data.csv")

with open (csvpath, newline="") as csvfile:
    pollreader = csv.reader(csvfile, delimiter = ',')
    print(pollreader)

    csv_header = next(pollreader)
    print(f"CSV Header: {csv_header}")

    #for row in pollreader:
     #   print (row[0])

# read dat into a dataframe using pandas

df = pd.read_csv("resources/pypoll_election_data.csv")
print(df.head(5))