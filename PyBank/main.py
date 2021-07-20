#Note most of code was provided by the UTSA instructor(Jeff Anderson) just modify to fit the assignment.

#Impot os module and reading CSV modules
import os
import csv

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

    # Read each row of data after the header
    rowcount = 0
    for row in csvreader:
# count the numer or Months by reading the number of rows.
        rowcount = rowcount + 1
        print("Total Months:", rowcount)
         

    