
import os
import csv

#define variables
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Path to collect data from Resources table
pypoll_election = os.path.join("Resources", "election_data.csv")

   
#Read in csv file
with open(pypoll_election, 'r') as csvfile:
    
    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
#set variables within rows
    voter = []
    county = []
    khan = []
    correy = []
    li =[]
    otooley = []
    candidates = []
    total_votes = 0

#start loop
    for row in csvreader:
    #count of total votes
        voter.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    total_votes = len(voter)
    
        #list of candidates
    candidates.append(row[2])

        #total number of votes of each candidate
    for candidate in candidates:
            if candidate == "Khan": 
                khan.append(candidate)
                khan_votes = len(khan)
            elif candidate == "Correy":
                correy.append(candidate)
                correy_votes = len(correy)
            elif candidate == "Li":
                li.append(candidate)
                li_votes = len(li)
            else:
                otooley.append(candidate)
                otooley_votes = len(otooley)
        
        #percentage votes for each candidates
            khan_votes_per = "{:.3%}".format(khan_votes/total_votes)
            correy_votes_per = "{:.3%}".format(correy_votes/total_votes)
            li_votes_per = "{:.3%}".format(li_votes/total_votes)
            otooley_votes_per = "{:.3%}".format(otooley_votes/total_votes)

   #determine winner
            result = {khan_votes: "Khan", correy_votes: "Correy", li_votes: "Li", otooley_votes: "O'tooley"}
            winner_votes = (result.get(max(result)))
    
#print the data
    
    print(f"Election Results")
    print(f"---------------------")
    print(f" Total Votes: {total_votes}")
    print(f"---------------------")
    print(f" Khan: {khan_votes_per}, ({khan_votes})")
    print(f" Correy: {correy_votes_per}, ({correy_votes})")
    print(f" Li: {li_votes_per}, ({li_votes})")
    print(f" O'Tooley: {otooley_votes_per}, ({otooley_votes})")
    print(f"---------------------")
    print(f" Winner: {winner_votes}")

    #export to txt file
    Election_analysis = os.path.join("Analysis", "Election_analysis.txt")
    with open(Election_analysis, "w",) as txtfile:
        txtfile.write(f" Election Results\n")
        txtfile.write(f"---------------\n")
        txtfile.write(f" Total Votes: {total_votes}\n")
        txtfile.write(f" ---------------\n")
        txtfile.write(f" Khan: {khan_votes_per}, ({khan_votes})\n")
        txtfile.write(f" Correy: {correy_votes_per}, ({correy_votes})\n")
        txtfile.write(f" Li: {li_votes_per}, ({li_votes})\n")
        txtfile.write(f" O'Tooley: {otooley_votes_per}, ({otooley_votes})\n")
        txtfile.write(f" ---------------\n")
        txtfile.write(f" Winner: {winner_votes}\n") 