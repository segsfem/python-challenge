import os
import csv
# Path to collect data from Resources table
Pybank_revenue = os.path.join("Resources", "budget_data.csv")

#Define functions and have it accept pybank as sole parameter
def print_average(pybank_data):

#assigning values to variables
    Date = int(pybank.data[0])
    Profit_Losses = int(pybank.data[1])

#Number of months on record
    total_months = sum(Date)

#Total profits in period
    total_profits = sum(Profit_Losses)

#Change in profits/losses
    change_profits = Profit_Losses.row() - Profit_Losses.row(1)

#Average change in profits/losses
    average_change_profits = change_profits/total_months

#Greatest increase change in profit
    best_profits = if (change_profits) > 1:
        print(max(change_profits))
        print(Date.row())
 
#Greatest decrease change in loss
    worst_loss = if (change_profits) < 1:
        print(max(change_profits))
        print(Date.row())

#Read in csv file
with open(Pybank_revenue, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

#loop through the data
    for row in csvreader
        print(total_months)
        print(total_profits)
        print(average_change_profits)
        print(best_profits)
        print(worst_loss)