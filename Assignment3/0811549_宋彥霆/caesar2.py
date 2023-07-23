"""
File: caesar.py
Name:0811549 宋彥霆
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    user input a string and this program can shift the alphabet
    to another string in order to encrypt
    """
    secret_number = int(input('Secret number: '))
    new_string = my_encrypt(secret_number)
    print('The deciphered string is: '+str(new_string))


def my_encrypt(s):
    input_string = input("What's the ciphered string?").upper()
    new_alphabet = ''                                   # record the new string which shifted from input string
    move_alphabet = ''                                  # record the 26 shifted alphabets
    for i in range(len(ALPHABET)):
        move_alphabet += ALPHABET[(len(ALPHABET) + s + i) % len(ALPHABET)]
    for i in range(len(input_string)):
        if input_string[i].isalpha():                   # to check if sting[i] is alphabet or not
            number = ALPHABET.find(input_string[i])
            new_alphabet += move_alphabet[number]
        else:                                           # if string[i] is not alphabet then print original one
            new_alphabet += input_string[i]
    return new_alphabet


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
