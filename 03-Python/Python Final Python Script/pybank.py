#import dependencies
import csv
import os

# Make a reference to the books.csv file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    #Set Values in Data Set
    months = []
    nettotal = []
    averagechange = 0
    greatestincrease = 0
    greatestdecrease = 0
    
    #read through each row of data after header
    csv_header = next(csvfile)
    row_num = 0
    for rows in csvreader:
        nettotal.append(rows[1])
        months.append(rows[0])
        row_num = row_num + 1
        
#Print Headline for Data
print("Financial Analysis")
print("----------------------------")

#Sum Total Number of Months in Budget Data
totalmonths = len(months)
#print total months
print("Total Months: " + str(totalmonths))

#Net total amount of "Profit/Losses"
#set profit to 0
profitloss = 0
for y in nettotal:
    #add column
    profitloss = profitloss + int(y)
#print total profit/loss
print("Total: $" + str(profitloss))

#calculate average revenue change
change = []

for x in range(1, len(nettotal)):
    #append change list
    change.append((int(nettotal[x]) - int(nettotal[x-1])))
    
    average = sum(change) / len(change)
 #print the average change   
print("Average change: " + "$" + str(round(average, 2)))

#Greatest increase max
greatestincrease = max(change)
#print greatest increase in profits
print("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "($" + str(greatestincrease) + ")")

#Greatest decrease min
greatestdecrease = min(change)
#print greatest decrease in profits
print("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "($" + str(greatestdecrease) + ")")

#create path for outbound text file
txtpath = os.path.join("kps-pybank_output.txt")

#write results to text file
with open(txtpath, "w") as  writefile:
    writefile.writelines("Financial Analysis\n")
    writefile.writelines("----------------------------\n")
    writefile.writelines("Total Months: " + str(totalmonths)+ "\n")
    writefile.writelines("Total Revenue: $" + str(profitloss)+ "\n")
    writefile.writelines("Average change: " + "$" + str(round(average, 2)) + "\n")
    writefile.writelines("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "($" + str(greatestincrease) + ")" + "\n")
    writefile.writelines("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "($" + str(greatestdecrease) + ")" +"\n")