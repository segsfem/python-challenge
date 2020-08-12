import os
import csv
import math
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
    best_profits = (change_profits) > 1
    print(Date.row())
    print(max(change_profits))
    
 
#Greatest decrease change in loss
    worst_loss = (change_profits) < 1
    print(Date.row())
    print(max(change_profits))
    

#Read in csv file
with open(Pybank_revenue, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

#loop through the data
    for row in csvreader:
        print(f" Total Months: {str(total_months)}")
        print(f" Total: {str(total_profits)}")
        print(f" Average Change: {str(average_change_profits)}")
        print(f" Greatest Increase in Profits: {str(best_profits)}")
        print(f" Greatest Decrease in Profits: {str(worst_loss)}")