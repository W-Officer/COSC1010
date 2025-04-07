#
# Name
# Date
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#variables
amount = 0.0
lines = 0.0
average = 0.0

#open the file & get number/loops.
try:
    myfile = open('Exception-Handling/numbers.txt', 'r')
    for line in myfile:
        number = int(line)
        amount += number
        lines += 1
except FileNotFoundError:
    print('Error: File not found.')
    #Exception handling for IO Errors.
except IOError:
    print("An input/output error has occured.")
    #Exception handling for Value Errors.
except ValueError as err:
    print('Error numbers not in numeric format.', err)
#close file
    myfile.close()

#get average
average = amount/lines

#print average
print(average)
