#-*- coding: UTF-8 -*-#
"""PyBank Homework Starter File."""

#---Dependencies---#
import csv
import os

#---Files to load and output---#
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

#---Define variables to track the financial data, add more variables to track other necessary financial data
total_months = 0
total_net = 0
changes = []
greatest_increase = {"date": None, "amount": float('-inf')} #Xpert Learning
greatest_decrease = {"date": None, "amount": float('inf')} #Xpert Learning

#---Open and read the csv---#
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    #---Skip the first row to avoid needing to append it---#
    first_row = next(reader)
    first_date, first_profit_loss = first_row[0], int(first_row[1])

    #---Track the total and net change---#
    total_months = 1 
    total_net = first_profit_loss
    previous_profit = first_profit_loss

    #---Process each row of data---#
    for row in reader:
        date, profit_loss = row[0], int(row[1])

        #---Track the total, net change, as well as update profit increases---#
        total_months += 1    
        total_net += profit_loss
        change = profit_loss - previous_profit
        changes.append(change)

        #---Calculate the greatest increase in profits, and decreases in losses---# #Xpert Learning Assistant
        if change > greatest_increase["amount"]:
            greatest_increase = {"date": date, "amount": change}
        if change < greatest_decrease["amount"]:
            greatest_decrease = {"date": date, "amount": change}

        #---Update previous profit for next pass through the rows---#
        previous_profit = profit_loss

#----Calculate the average net change across the months---#
average_change = sum(changes)/len(changes)

#---Generate the output summary, print the output---#
output = (
    "Financial Analysis\n\n"
    "-----------------------------\n\n"
    f"Total Months: {total_months}\n\n"
    f"Total: ${total_net}\n\n"
    f"Average Change: ${average_change: .2f}\n\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n\n"
)

print(output)

#---Write the results to a text file---#
with open(file_to_output, "w") as file:
    file.write(output)
