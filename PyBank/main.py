

import os
import csv
import numpy as np
import pandas as pd

csvpath = os.path.join("resources", "pybank_budget_data.csv")

#initialize empty lists
months = []
profit = []
profit_1 = []
profit_2 = []

# open pybank_budget file, create budget reader object

with open (csvpath, newline="") as csvfile:
    budgetreader = csv.reader(csvfile, delimiter = ',')
    print(budgetreader)

# iterate through rows, skipping first (header) row.  Make list of months and list of profits.  We make three lists. 1 - original profi/loss.  
# profit_2 will have beginning value ;opped off, profit_1 will have end popped off.  This aligns 1st mth w 2nd month etc, 
# so when I subtratct list 1 from list 2, t will give the diff between month2 and month 1 etc.

    i = 0
    for row in budgetreader:
        if i > 0:
            months.append(row[0])
            profit.append(float(row[1]))
            profit_1.append(float(row[1]))
            profit_2.append(float(row[1]))
        i += 1    

# see above comment for why all the popping            
profit_1.pop()
profit_2.pop(0)

# convert lists to arrays using numpy asarray() method
profit_1 = np.asarray(profit_1)
profit_2 = np.asarray(profit_2)

#subtract all months profits (2-1, 3-2, 4-3, etc.)
diffs = np.subtract(profit_2, profit_1)

#check that arrays align and diffs look right
#print(profit_2)
#print(profit_1)
#print(diffs)

# calculate number of months, mean, sum, highest month-month change (diffs max), highest loss (diffs min), 
num_months = len(profit)
profit_mean = round(np.mean(diffs),2)
total = round(sum(profit), 2)
great_increase = round(max(diffs))
least_increase = round(min(diffs))

# To get month corresponding to greatest and least differences, find index of greatest diff in the diffs array, convert it to int for use later.
#  The result of np.where is a list, the index is at [0].   Use this index (+1) to find month in months list.
where_great_diff = np.where(diffs == max(diffs))
great_diff_index = int(where_great_diff[0])

# find index of least diff (greatest decrease) in the diffs array, convert it to int for use later.  the result of np.where is a list, the index is at [0]
where_least_diff = np.where(diffs == min(diffs))
least_diff_index = int(where_least_diff[0])

#check index
#print(great_diff_index)
 #find corresponding month in months list.  Need to add 1 because diffs array is offset from original list by 1 (because of above pop)

great_month = months[great_diff_index + 1]
#print("great: " + great_month) 

#print(great_diff_index)
least_month = months[least_diff_index + 1]
#print("least: " + least_month) 

print("------------------")
print ("Financial Analysis")
print("------------------")
print ("Total Months: " + str(num_months))
print("Total: $" + str (total))
print("Average change $" + str(profit_mean))
print("Greatest Increase in Profits: $" + str(great_increase) + ")")
print("Greatest Decrease in Profits: $" + str(least_increase) + ")")
print("------------------")
 
