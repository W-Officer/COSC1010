#
# Wynn Officer
# 4/9/25
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

#function for loading responses
def load_responses():
    #load responses from file
    try:
        with open('Magic-8-Ball/8_ball_responses.txt', 'r') as file:
            responses = file.readlines()

        return responses
    #check for any IOError
    except IOError:
        print('Error: Could not read file.')
    
#function for running the game
def main():
    responses = load_responses()

    while True:
        question = input("Ask a yes or no question (or type 'quit' to exit): ")

        #check if user wants to quit
        if question == 'quit':
            print('Thanks for playing!')
            break

        #Randomly select responses
        response = random.choice(responses)
        print('The Magic 8 Ball says: ', response)

#start the game
main()