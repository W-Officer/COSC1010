#
# Wynn Officer
# 4/19/25
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#call user input
usr_string = input('Enter a sentence: ')

#split the sentence into words
words = usr_string.split()

#create a list
words_pig = []

#Convert word into pig latin
for word in words:
    #take first letter and add it to the end, also add "ay"
    pig_word = word[1:] + word[0] + "Ay"

    #put word into list
    words_pig.append(pig_word)

pig_latin_sentence = ' '.join(words_pig)

#print the function
print('Pig Latin: ', pig_latin_sentence)