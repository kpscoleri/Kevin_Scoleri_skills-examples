#import dependencies
import os
import csv

# Make a reference to the books.csv file path
csvpath = os.path.join("..", "Resources", "election_data.csv")

#define variables
total_votes = 0
uniqcandidate = []
candidate_vote_count = []

#open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read through each row of data after header
    csv_header = next(csvreader)
    csv_header = next(csvfile)

    for row in csvreader:
        #Add Total votes cast
        total_votes = total_votes + 1
        #compile the list of candidates
        candidates = (row[2])
        #compile list of candidates
        if candidates in uniqcandidate:
            candidatesdex = uniqcandidate.index(candidates)
            candidate_vote_count[candidatesdex] = candidate_vote_count[candidatesdex] + 1
        else:
            uniqcandidate.append(candidates)
            candidate_vote_count.append(1)
#print header
print("Election Results")
print("----------------------------")
#print total votes
print(f"Total Votes: {total_votes}")
print("----------------------------")
percent = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(uniqcandidate)):
    #use loop to get vote percentage
    vote_percent = round(candidate_vote_count[x]/total_votes*100, 2)
    percent.append(vote_percent)
    #determine highest vote count
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x
for x in range(len(uniqcandidate)):
    print(f"{uniqcandidate[x]} : {percent[x]}% ({candidate_vote_count[x]})")
    
election_winner = uniqcandidate[max_index] 
print("----------------------------")
print(f"Election winner: {election_winner}")
print("----------------------------")

#create path for outbound text file
txtpath = os.path.join("kps-pypoll_output.txt")

#write results to text file
with open(txtpath, "w") as  writefile:
    writefile.writelines("Election Results\n")
    writefile.writelines("----------------------------\n")
    writefile.writelines(f"Total Votes: {total_votes}\n")
    writefile.writelines("----------------------------\n")
    for x in range(len(uniqcandidate)):
        writefile.writelines(f"{uniqcandidate[x]} : {percent[x]}% ({candidate_vote_count[x]})" + "\n")
    writefile.writelines("----------------------------\n")
    writefile.writelines(f"Election winner: {election_winner}" + "\n")
    writefile.writelines("----------------------------\n")
