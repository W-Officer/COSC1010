#
# Wynn Officer
# 4/6/25
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#variables
amount = 0.0
lines = 0.0
average = 0.0
numbers = 0.0

#open the file & get number/loops.
try:
    with open('Exception-Handling/numbers.txt', 'r') as file:

        for line in file:
            try:
                numbers = int(line)
                amount += numbers
                lines += 1
            except ValueError as err:
                print('Error: Numbers not in numeric format. ', err)
    
    #Exception handling for IO Errors.
except IOError:
    print("An input/output error has occured.")
    #Exception handling for Value Errors.

#get average and print
if numbers:
    average = amount/lines
    print('The average is:', average, '. ')
else:
    print('Error: could not read the file numbers.txt')
