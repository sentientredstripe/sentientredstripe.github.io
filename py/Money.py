# -*- coding: latin-1 -*-
# In this program you will prompt the user for two inputs:
#
# The first is Total_Savings
# The second is Total_Expenses
#
# Declare and use Variables for each input.
#
# Next based on the following:
# If Total_Savings > Total Expenses.
# Display a message that they have “Money in the bank!”
#       if Difference is less than $1,000 state a message saying “Need to Save”
#       if Difference is $1,000 or more and less than $10,000 state a message saying
#      “Save for Emergency”
#       if Difference is $10,000 or more state a message “Time for vacation”
# note Difference = Total_Savings - Total Expenses
#
# If Total_Savings <= Total Expenses
#  Display message that we have “No money in the Bank!!”
#       if Difference is less than $1,000 state a message saying “Almost out of debt!”
#       if Difference is $1,000 or more and less than $5,000 sate message saying “Need help”
#       if Difference is $5,000 or more state a message “Bankruptcy looming”
#  note Difference = Total Expenses - Total_Savings

totalSavings = float(input("Enter the dollar amount of your savings: $"))
totalExpenses = float(input("Enter the dollar amount of your expenses: $"))

if totalSavings > totalExpenses:
   print("Money in the bank!")
   if totalSavings - totalExpenses < 1000:
       print("However, you need to save.")
   if totalSavings - totalExpenses > 1000 and totalSavings - totalExpenses < 10000:
       print("You have a good amount of money but you should save for an emergency.")
   if totalSavings - totalExpenses >= 10000:
       print("Time for a vacation!")
elif totalSavings <= totalExpenses:
   print("No money in the bank!")
   if totalExpenses - totalSavings < 1000:
       print("Almost out of debt!")
   if totalExpenses - totalSavings >= 1000 and totalExpenses - totalSavings < 5000:
       print("You need help.")
   if totalExpenses - totalSavings >=5000:
       print("Bankruptcy looming.")