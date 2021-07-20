#Note most of code was provided by the UTSA instructor(Jeff Anderson) just modify to fit the assignment.

#Impot os module and reading CSV modules
import os
import csv

# Creating Variable to hold the data
profit = []
monthly_changes = []
rowcount = 0
TotalProfit = 0
AverageProfit = 0
AverageChange = 0
LostProfit = 0
GainProfit = 0

#locating the file path of reading the csv data
PyBankdataFile = os.path.join('Resources', 'budget_data.csv')

#Opens and reads csv file
with open(PyBankdataFile, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
     #checking if this prints the Header of the CSV file.
    print(f"CSV Header: {csv_header}")

    # Create variables to help find the profit, number of rows
    for row in csvreader:
    # count the numer or Months by reading the number of rows.
        rowcount = rowcount +1
        print("Total Months:", rowcount)
     #The net total amount of "Profit/Losses" over the entire period
        profit.append(row[1])
        TotalProfit = TotalProfit + int(row[1])
        print('Total Profit is: $', TotalProfit)
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        AverageProfit = TotalProfit / rowcount
        print('Average Profit is $', AverageProfit)
        if float(row[1]) <=0:
            LostProfit = LostProfit + int (row[1])
        elif float(row[1]) >0:
            GainProfit = GainProfit + int(row[1])
        else:
            AverageChange = LostProfit + GainProfit
            print('The Average Change: $',AverageChange)

# Open the file using "write" mode. Specify the variable to hold the contents
with open('Results_PyBank', 'w') as text:
    text.write("Total Months: + str(rowcount)\n")
        




  











         

    