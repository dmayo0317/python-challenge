#Note most of code was provided by the UTSA instructor(Jeff Anderson) just modify to fit the assignment.

#Impot os module and reading CSV modules
import os
import csv

# Creating Variable to hold the data
rowcount = 0
TotalProfit = 0
AverageProfit = 0
AverageChange = 0
LostProfit = 0
GainProfit = 0

#locating the file path of reading the csv data
PyPolldataFile = os.path.join('Resources', 'election_data.csv')

#Opens and reads csv file
with open(PyPolldataFile, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents

    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
     #checking if this prints the Header of the CSV file.
    print(f"CSV Header: {csv_header}")

    # Create variables to help find the profit, number of rows
    for row in csvreader:

        break
