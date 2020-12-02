

import os
import csv
import numpy as np
import pandas as pd

csvpath = os.path.join("resources", "pybank_budget_data.csv")


profit_1 = []
profit_2 = []

with open (csvpath, newline="") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter = ',')
    print(budgetreader)

    i = 0
    for row in budgetreader:
        if i > 0:
            profit_1.append(float(row[1]))
            profit_2.append(float(row[1]))
        i += 1    
            
profit_1.pop()

profit_2.pop(0)


profit_1 = np.asarray(profit_1)
profit_2 = np.asarray(profit_2)


diffs = np.subtract(profit_2, profit_1)

#print(profit_2)
#print(profit_1)
#print(diffs)
print (round(np.mean(diffs),2))
    
