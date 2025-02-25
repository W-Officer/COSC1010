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
for week in range(1,5):
    print('Expenses for the week: ', week)
    expenses = int(input())
    totalExpenses += expenses

#Displaying the total amount of budget is left
if totalExpenses > budget:
    print('Expenses have exeeded budget by: $', format(totalExpenses - budget,'.2f'))
elif budget > totalExpenses:
    print('Budget have exeeded expense by: $', format(budget - totalExpenses,'.2f'))
else:
    print('Budget and expenses are equal.')


# Use comments liberally throughout the program. 