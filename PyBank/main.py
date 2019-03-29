import os
import csv

budget_data = os.path.join('..', 'BankResources', 'budget_data.csv')

Month = []
PL = []
Change = []

with open (budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    for row in csvreader:
        Month.append(row[0])
        PL.append(int(row[1]))
    
    for i in range(len(PL)-1):
        Change.append(PL[i+1]-PL[i])

Total_Months = len(Month)
Total_PL = sum(PL)
Total_Change = sum(Change)

Increase_max = max(Change)
Decrease_max = min(Change)

Month_max = Change.index(max(Change))+1
Month_min = Change.index(min(Change))+1

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months : {Total_Months}")
print(f"Total : ${Total_PL}")
print(f"Average Change : ${round(Total_Change/len(Change), 2)}")
print(f"Greatest Increase in Profits: {Month[Month_max]} (${(str(Increase_max))})")
print(f"Greatest Decrease in Profits: {Month[Month_min]} (${(str(Decrease_max))})")

output = open("output.txt","w")
line1 = "Financial Analysis"
line2 = "-------------------------------"
line3 = f"Total Months : {Total_Months}"
line4 = f"Total : ${Total_PL}"
line5 = f"Average Change : ${round(Total_Change/len(Change), 2)}"
line6 = f"Greatest Increase in Profits: {Month[Month_max]} (${(str(Increase_max))})"
line7 = f"Greatest Decrease in Profits: {Month[Month_min]} (${(str(Decrease_max))})"
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
