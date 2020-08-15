
import os
import csv


#define variables
total_votes = 0
list_candidates = []
candidates_votes = 0
voter_id = 0
county = 0
winner = []

# Path to collect data from Resources table
pypoll_election = os.path.join("Resources", "election_data.csv")

#Define functions and have it accept pybank as sole parameter
def print_winner(pypoll_election):

#assigning values to variables
    Voter_ID = int(pypoll_election[0])
    County = int(pypoll_election[1])
    Candidate = str(pypoll_election[2])

#Read in csv file
with open(pypoll_election, 'r') as csvfile:
    
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    row = next(csvreader)

#set variables within rows
    list_candidates = (row[2])
    count_of_votes = (row[2])
    total_votes = int(row[0])
    highest_votes = int(row[0])
    votes_per_candidate =(row[2])
    
#start loop
    for row in csvreader:
        #count of total votes
        voter_id += int(row[0])

        #list of candidates
        list_candidates = list(row[2])
        list_candidates.append(row[2])

        #percentage votes for each candidates
        per_count_of_votes = (sum(len(list_candidates))/voter_id) * 100

        #total number of votes of each candidate
        if int(row[1]) > best_profit:
            best_profit = int(row[1])
            best_profit_month = row[0]

        #winner
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