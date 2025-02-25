#
# Wynn Officer
# 2/25/25
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
bugsCollected = 0.0
bugs = 0.0
# Get number of bugs collected each day using a for loop.
for day in range(1,6) :
    print ('Bugs collected on day', day)
    bugs = int(input())
    bugsCollected += bugs
# Display the total number of bugs collected.
print ('You have collected a total of', bugsCollected, 'bugs.')