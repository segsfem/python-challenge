import os
import csv

# Path to collect data from Resources table
Pybank_revenue = os.path.join("Resources", "budget_data.csv")

#define variables
total_months = 0
total_profits = 0
change_profits = 0
average_change_profits = 0
months = [0]
months_change = [0]
months_count = [0]

#Define functions and have it accept pybank as sole parameter
def print_average(pybank_data):

#assigning values to variables
    Date = str(pybank.data[0])
    Profit_Losses = int(pybank.data[1])

#set variables within rows
    net_profit = int(row[1])
    previous_profit = int(row[1])
    best_profit = int(row[1])
    best_profit_month = int(row[0])
    worst_loss =int(row[1])
    worst_loss_month = int(row[0])

#start csvreader
    for row in csvreader:
        #count of total months
        months.append(row[0])
        months_count = len(months)

        #total profits/losses for period
        total_profits += int(row[1])

        #average change of profits in period
        change_profits = int(row[1]) - previous_profit
        months_change.append(change_profits)
        average_change_profits = sum(months_change)/months_count

        #find the greatest increase in profits
        if int(row[1]) > best_profit:
            best_profit = int(row[1])


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