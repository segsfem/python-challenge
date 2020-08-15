import os
import csv


#define variables
total_months = 0
total_profits = 0
change_profits = 0
average_change_profits = 0
months = [0]
months_change = [0]
months_count = [0]

# Path to collect data from Resources table
Pybank_revenue = os.path.join("Resources", "budget_data.csv")

#Define functions and have it accept pybank as sole parameter
def print_average(pybank_data):

#assigning values to variables
    Date = str(pybank.data[0])
    Profit_Losses = int(pybank.data[1])

#Read in csv file
with open(Pybank_revenue, 'r') as csvfile:
    
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    row = next(csvreader)

#set variables within rows
    net_profit = int(row[1])
    previous_profit = int(row[1])
    best_profit = int(row[1])
    best_profit_month = (row[0])
    worst_loss =int(row[1])
    worst_loss_month = (row[0])

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
            best_profit_month = row[0]

        #find the worst decrease in profits
        if int(row[1]) < worst_loss:
            worst_loss = int(row[1])
            worst_loss_month = row[0]

        highest_profit = max(months_change)
        worst_loss = min(months_change)

    #loop through the data
    
        print(f"Financial Analysis")
        print(f"---------------------")
        print(f" Total Months: {months_count}")
        print(f" Total: ${total_profits}")
        print(f" Average Change: ${average_change_profits}")
        print(f" Greatest Increase in Profits: ${highest_profit}")
        print(f" Greatest Decrease in Profits: ${worst_loss}")