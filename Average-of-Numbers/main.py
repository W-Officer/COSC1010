#
# Wynn Officer
# 3/31/25
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#variables
amount = 0.0
lines = 0.0
average = 0.0

#open the file
myfile = open('/workspaces/COSC1010/Average-of-Numbers/numbers.txt', 'r')

#get amount of number and how many loops
for line in myfile:
    number = int(line)
    amount += number
    lines += 1
    
#close file
myfile.close()

#get average
average = amount/lines

#print average
print(average)
