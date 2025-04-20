#
# Wynn Officer
# 4/19/25
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#main function.
def main():
    #get the string from user.
    user_str = input('Enter a string of characters: ')

    #print the vowels and constantants
    print('That string has', num_vowels(user_str), 'vowels and', \
          num_constantants(user_str), 'constantants.')

#vowel function.
def num_vowels(s):
    #make a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    #starting accumulator
    v_count = 0

    #count the vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    #return vowel count.
    return v_count

#constantant function.
def num_constantants(s):
    #make another vowel list
    vowels = ['a', 'e', 'i', 'o', 'u']

    #start accumulator
    c_count = 0

    #count the constantants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    #return the consonant count.
    return c_count

#call main function
main()