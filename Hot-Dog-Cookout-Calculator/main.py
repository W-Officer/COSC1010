#
# Wynn Officer
# 2/20/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
#Constants for hot dogs
HOT_DOGS_PER_PACKAGE = 10
HOT_DOG_BUNS_PER_PACKAGE = 8
#Variables
numberPeople = 0    #number of people attending
hdPerPerson = 0     #number of hotdogs and buns per person
total = 0           #Total number of hog dogs & buns needed
minDogs = 0         #minimum number of hog dogs needed
minBuns = 0         #Minimum mnumber of buns needed
dogsLeft = 0        #Hots Dogs left
bunsLeft = 0        #Hot dog buns left

#People attending the cookout & how many hotdogs they are given
numberPeople = int(input('Enter the number of people attending the cookout: '))
hdPerPerson = int(input('Enter the umber of hotdogs per person: '))

#calculate how many hotdogs you need
total = numberPeople * hdPerPerson

#calculate how many packages of hot dogs you need
minDogs = total // HOT_DOGS_PER_PACKAGE

#Determine if you need more than one package of Hot Dogs
if minDogs > 0:
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    if dogsLeft != 0:
        minDogs += 1

#set the min number of packages of hot dogs to one for numberPeople reguiring less than one package.
else:
    minDogs = 1

#Determine leftovers of hot dogs
dogsLeft = (HOT_DOGS_PER_PACKAGE * minDogs) - total

#calculate how many packages of hot dog buns you need
minBuns = total // HOT_DOG_BUNS_PER_PACKAGE

#Determine if you need more than one package of Hot Dog Buns
if minBuns > 0:
    bunsLeft = total % HOT_DOG_BUNS_PER_PACKAGE

    if bunsLeft != 0:
        minBuns += 1

#Set the min number of packages of hot dog buns to one for numberPeople requiring less than one package.
else:
    minBuns = 1

#Determine Leftovers of hot dog buns.
bunsLeft = (HOT_DOG_BUNS_PER_PACKAGE * minBuns) - total

#Display the minimum packages of hot dogs needed
print('Minimum packages of hot dogs needed: ', minDogs)

#Display the minimum packages of hot dog buns needed
print('Minimum packages of hot dog buns needed: ', minBuns)

#Display the leftovers of hot dogs left
print('Number of hot dogs leftover: ', dogsLeft)

#Display the leftovers of hot dog buns left
print('Number of hot dog buns leftover: ', bunsLeft)