#
# Wynn Officer
# 4/24/25
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

# Initialize dictionary
capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
            'Arizona':'Phoenix', 'Arkansas':'Little Rock',
            'California':'Sacramento', 'Colorado':'Denver',
            'Connecticut':'Hartford', 'Delaware':'Dover',
            'Florida':'Tallahassee', 'Georgia':'Atlanta',
            'Hawaii':'Honolulu', 'Idaho':'Boise',
            'Illinois':'Springfield', 'Indiana':'Indianapolis',
            'Iowa':'Des Moines', 'Kansas':'Topeka',
            'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
            'Maine':'Augusta', 'Maryland':'Annapolis',
            'Massachusetts':'Boston', 'Michigan':'Lansing',
            'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
            'Missouri':'Jefferson City', 'Montana':'Helena',
            'Nebraska':'Lincoln', 'Nevada':'Carson City',
            'New Hampshire':'Concord', 'New Jersey':'Trenton',
            'New Mexico':'Santa Fe', 'New York':'Albany',
            'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
            'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
            'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
            'Rhode Island':'Providence', 'South Carolina':'Columbia',
            'South Dakota':'Pierre', 'Tennessee':'Nashville',
            'Texas':'Austin', 'Utah':'Salt Lake City',
            'Vermont':'Montpelier', 'Virginia':'Richmond',
            'Washington':'Olympia', 'West Virginia':'Charleston',
            'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    
def main():
    # Local variables
    state_caps = list(capitals.keys())
    correct = 0
    incorrect = 0

    #quiz the user
    while True:
        #get an entry at random from the dictionary
        state = random.choice(state_caps)

         #ask the question?
        print('What is the capital of ', state, '? (Type "quit" to end the quiz): ', end='')
        response = input().strip()

        #check if user wants to quit
        if response.lower()  == 'quit':
            break

        #indicitate correct response
        correct_answer = capitals[state]
        if response.lower() == correct_answer.lower():
            correct += 1
            print('Correct!')
        
        #indicate an incorrect response
        else:
            incorrect += 1
            print('Incorrect.')
        
    
#print the results
    print('Correct responses:', correct)
    print('Incorrect responses:', incorrect)


# Call the main function.
main()
