import os
import csv
# Path to collect data from Resources table
Banking_csv = os.path.join('..', 'Resources', 'budget_data.csv' )

#Define functions and have it accept pybank as sole parameter
def print_average(pybank_data):

#assigning values to variables
Date = int(pybank.data[0])
Profit/Losses = int(pybank.data[1])

#Number of months on record
total_months = sum(Date)

#Total profits in period
total_profits = sum(Profit/Losses)

#Average profits in period
average_profits = total_months/total_profits


#Read in csv file
with open(Banking_csv, 'r') as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
