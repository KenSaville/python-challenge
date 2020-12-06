# python-challenge

This is the final github page for "python-challenge".  A homework assignment for MSU-data bootcamp.

This project includes two parts:  PyBank and PyPoll

## PyBank

The goal of pybank was to open a file containing profit/loss data for several months (86 total) and to carry out a few calculations.

The results of these were then printed to the screen and to a file (in the analysis folder)

Most steps were straight forward - i.e. calculating total months, total overall profit

Calculating change from month to month was a little trickier.

To do this, I created a list of profit values for each month, then converted these lists to numpy arrays so I could subtract one list form another, cteating a new array that contained the differences between months.

The lists had to first be offset so that month 1 was subtracted from month 2, 2 from 3 etc.  To do this I 'popped' off the last month of list 1 and the first month of list 2.  This aligned the lists so that the appropriate subtractions would take place.  

## PyPoll

This challenge required identify all of the candidates in an election, tallying up the total votes and vote percentages, determing the winner, and displaying the results on the terminal and in a file.

A main part of this was creating a dictionary with the names of the candidates as key and a list with votes and percent for each candidate.

A challenge was to print these out in a neat forma.  Initial attempts to print had the results unaligned with each other.  I found f string formatting and figured out how to use that.  The results look pretty good.

