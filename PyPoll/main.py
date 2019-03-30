import os
import csv

election_data = os.path.join('..', 'PollResources', 'election_data.csv')

Candidate = []
VoteAmount = []
VotePercent = []

Total_Votes = 0

with open(election_data, newline = '') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        Total_Votes += 1

        if row[2] not in Candidate:
            Candidate.append(row[2])
            index = Candidate.index(row[2])
            VoteAmount.append(1)
        else:
            index = Candidate.index(row[2])
            VoteAmount[index] += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    for votes in VoteAmount:
        percentage = "%.3f%%" % round(((votes/Total_Votes)*100))
        VotePercent.append(percentage)    

Winner_votes = max(VoteAmount)
Index = VoteAmount.index(Winner_votes)
Winner = Candidate[Index] 

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------------")
for i in range(len(Candidate)):
    print(f"{Candidate[i]}:{VotePercent[i]} ({VoteAmount[i]}) ")
print("-------------------------------")
print(f"Winner: {Winner}")
print("-------------------------------")
    
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {Total_Votes}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(Candidate)):
    line = (f"{Candidate[i]}: {VotePercent[i]} ({VoteAmount[i]})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {Winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
