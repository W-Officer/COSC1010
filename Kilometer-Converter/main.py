#
# Wynn Officer
# 3/6/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#constants
CONVERSION_FACTOR = 0.6214

#variable
miles = 0.0
kilometers = 0.0

#define main
def main():
    #Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    #display the distance converted to miles
    show_miles(kilometers)

#define show_miles
def show_miles (km):
    #calcuate miles
    miles = km * CONVERSION_FACTOR

    #display the miles
    print(km, 'kilometers equals', miles, 'miles.')

#call the main function
main()
