

import os
import csv
import numpy as np
import pandas as pd

csvpath = os.path.join("resources", "pybank_budget_data.csv")

with open (csvpath, newline="") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter = ',')
    print(budgetreader)

    csv_header = next(budgetreader)
    print(f"CSV Header: {csv_header}")

    #for row in budgetreader:
     #       print(row[0])

df = pd.read_csv("resources/pybank_budget_data.csv")
print(df.head(5))

print(df['Date'].head(5))

print(df[1].head(5))





    
