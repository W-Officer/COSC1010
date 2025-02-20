#
# Wynn Officer
# 2/20/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
lengthA = 0.0
lengthB = 0.0
widthA = 0.0
widthB = 0.0
areaA = 0.0
areaB = 0.0
# Get length A
lengthA = int(input('Length of the first rectangle: '))
# Get width A
widthA = int(input('Width of the first rectangle: '))
# Get length B
lengthB = int(input('Length of the Second rectangle: '))
# Get width B
widthB = int(input('Width of the Second rectangle: '))
# Calculate area A
areaA = lengthA * widthA
# Calculate area B
areaB = lengthB * widthB
# Print area comparison using if-elif-else statements
if areaA > areaB:
    print('Rectangle 1 has the greater area.')
elif areaB > areaA:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')