#
# Wynn Officer
# 2/25/25
# Budget Analysis Programming Project
# COSC 1010
#
#Variables for use
budget = 0.0
expenses = 0.0
totalExpenses = 0.0

#Budget for the month input
budget = int(input('Input budget for this month: '))

#expenses for the month
while True:
        expense = float(input("Enter expense amount (or '0' to finish): "))
        if expense == 0:
            break  # Exit loop if user enters 0
        totalExpenses += expense

#Displaying the total amount of budget is left
if totalExpenses > budget:
    print('Expenses have exeeded budget by: $', format(totalExpenses - budget,'.2f'))
elif budget > totalExpenses:
    print('Budget have exeeded expense by: $', format(budget - totalExpenses,'.2f'))
else:
    print('Budget and expenses are equal.')

# Use comments liberally throughout the program. 