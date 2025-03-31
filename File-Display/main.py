#
# Wynn Officer
# 3/31/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#Open the file if the file exists
myfile = open('/workspaces/COSC1010/File-Display/numbers.txt', 'r')

#display the files contents
for line in myfile:
    number = int(line)
    print(number)

#close file
myfile.close()
