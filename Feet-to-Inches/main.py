#
# Wynn Officer
# 3/6/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

#constants
INCHES_PER_FOOT = 12

#variables
feet_to_inches = 0.0
feet = 0.0

#function
def main():
    #User imput
    feet = int(input('Enter the number of feet: '))

    #print the results
    if feet == 1:
        print(feet, 'foot equals', feet_to_inches(feet), 'inches.')
    elif feet > 1:
        print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

#feet_to_inches converted
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#re call the main
main()