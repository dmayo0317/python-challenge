#Note most of code was provided by the UTSA instructor(Jeff Anderson) just modify to fit the assignment.

#Impot os module and reading CSV modules
import os
import csv

# Creating Variable to hold the data
rowcount = 0
CanList=[]
winner = 0



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

#For loop to look through the Data file
    for row in csvreader:
        #counts the number of votes
        rowcount = rowcount +1
        #Go into the Canditateslist
        CanList.append(row[2])

        print("Total Votes is", rowcount)

with open('Results_PyPoll', 'w') as text:
    text.write(f" Total Votes is: {rowcount}\n")

#Notes to Grader, I did not get enought time to ask for help thus incomplete. 
#I will request for a resubmission.
       

