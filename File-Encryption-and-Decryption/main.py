#
# Wynn Officer
# 4/26/25
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#define codes
codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '8', 
    'D': '&', 'd': '1', 'E': '!', 'e': '0', 'F': '^', 'f': '2',
    'G': '*', 'g': '3', 'H': '(', 'h': '4', 'I': ')', 'i': '5',
    'J': '_', 'j': '6', 'K': '+', 'k': '7', 'L': '=', 'l': 'L',
    'M': '-', 'm': ':', 'N': ';', 'n': 'z', 'O': '.', 'o': ',',
    'P': '/', 'p': '?', 'Q': '<', 'q': '>', 'R': '[', 'r': ']',
    'S': '{', 's': '}', 'T': 'd', 't': 'b', 'U': 'm', 'u': 'x',
    'V': 'v', 'v': 'f', 'W': 'o', 'w': 'u', 'X': 'k', 'x': 'l',
    'Y': 'a', 'y': 's', 'Z': 'B', 'z': 'Z', ',': 'O', '.': 'I',
    '1': 'Q', '2': 'W', '3': 'E', '4': 'R', '5': 'A', '6': 'S',
    '7': 'D', '8': 'F', '9': 'C', '0': 'G', '-': 'N'
}
#reverse the codes
reverse_codes = {v: k for k, v in codes.items()}

#encryption program to encrypt text.txt
def encryption():
    try:
        with open("File-Encryption-and-Decryption/text.txt", 'r') as infile: #open text to read the contents
            text = infile.read()

        encrypted = "" #encrypt the text
        for char in text:
            encrypted += codes.get(char, char)

        #write the encrypted files.
        with open("File-Encryption-and-Decryption/encrypted.txt", 'w') as outfile:
            outfile.write(encrypted)

        print('Encryption saved to encrypted.txt')

    except FileNotFoundError: #add exception to the file not being found
        print('Error: File not found!')

#define the program to decypher encrypted.txt.
def decryption():
    try:
        with open("File-Encryption-and-Decryption/encrypted.txt", 'r') as infile:
            text = infile.read()

        decrypted = "" #decrypt the text
        for char in text:
            decrypted += reverse_codes.get(char, char)

        #print the outcome
        print('Text decrypted: ', decrypted)

    except FileNotFoundError: #add exception to the file not being found
        print('Error: File not found')

#define main program to offer a choice
def main():
    choice = input('Would you like to encrypt or decrypt file? (1 for encrypt, 2 for decrypt) ')

    if choice == '1': #run the encryption program
        encryption()
        
    elif choice == '2': #run the decryption program
        decryption()

#call the main program
main()