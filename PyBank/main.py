import os
import csv


#define variables
total_months = 0
total_profits = 0
change_profits = 0
average_change_profits = 0
months = []
months_change = []
months_count = []

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

#start loop
    for row in csvreader:
        #count of total months
        months.append(row[0])
        months_count = len(months) + 1

        #total profits/losses for period
        total_profits += int(row[1])

        #average change of profits in period
        change_profits = int(row[1]) - previous_profit
        months_change.append(change_profits)
        previous_profit = int(row[1])
        average_change_profits = (sum(months_change)/len(months_change))

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
        print(f" Average Change: ${average_change_profits: .2f}")
        print(f" Greatest Increase in Profits: {best_profit_month}, ${highest_profit}")
        print(f" Greatest Decrease in Profits: {worst_loss_month}, ${worst_loss}")

        #export to txt file
        Bank_analysis = os.path.join("Analysis", "Bank_analysis.txt")
        with open(Bank_analysis, "w",) as txtfile:
            txtfile.write(f" Financial Analysis\n")
            txtfile.write(f"---------------\n")
            txtfile.write(f" Total Months: {months_count}\n")
            txtfile.write(f" Total: ${total_profits}\n")
            txtfile.write(f" Average Change: ${average_change_profits: 2f}\n")
            txtfile.write(f" Greatest Increase in Profits: {best_profit_month}, ${highest_profit}\n")
            txtfile.write(f" Greatest Decrease in Profits: {worst_loss_month}, ${worst_loss}\n") 