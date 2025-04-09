#
# Wynn Officer
# 4/9/25
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

MAX_DIGITS = 7
START = 0
END = 9

#function
def main():
    #create the list of number
    numbers = [0] * 7

    #populate with random numbers
    for index in range(MAX_DIGITS) :
        numbers[index] = random.randint (START, END)

    #print the numbers
    print('The Lottery numbers are:')
    for index in range(MAX_DIGITS) :
        print(numbers[index], end='')
    print()

#call the function
main()

