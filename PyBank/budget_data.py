import os
import csv

# Path to collect data from resource folder

budget_data.csv = os.path.join( "PyBank\Resources", "budget_data.csv" )



# Lists to store Data

total_months = []
total_profit_loss = []
average_change = []
greatest_increase = []
greatest_decrease = []

# Set initial values for variables

count = 0
total_profit_loss = 0
average_change = 0
greatest_decrease = 0
greatest_increase = 0


# Read the csv file

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Create variables for each column

    Date = str(budget_data [0])
    Profit_Losses = int(budget_data [1])

# Total months included in dataset use count to count the rows

    for row in csvreader:
        count = count + 1

# Net total amount of profit/losses over entire period

    sum total_profit_loss = 



