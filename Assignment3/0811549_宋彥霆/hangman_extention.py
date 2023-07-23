"""
File: hangman.py
Name:0811549   宋彥霆
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Players have N_TURNS chances to try and win hangman game.
    """
    answer = random_word()
    flag = 0                                        # number of guess left is N_TURN-flag
    old_box = ''                                    # string  that store player guess answer
    new_box = ''                                    # string that store player guess temporarily
    print('You word looks like: ', end='')
    for i in range(len(answer)):
        old_box += '-'
    print(old_box, end='')
    print("")                                       # make a new line
    print('You have ' + str(int(N_TURNS) - flag) + ' guesses left.')
    extension(flag)                                 # # print image
    input_ch = input('Your guess:')
    while not input_ch.isalpha() or len(input_ch) != 1:         # if input non-alphabet,input again.
        print('illegal format.')                                # if input more than one character,input again.
        input_ch = input('Your guess:')
    input_ch = input_ch.upper()                                 # make input character upper


    """
    This while loop will stop when player guess the whole answer or 
    guess wrong N_turns times.
    """
    while True:
        for i in range(len(answer)):
            if input_ch == answer[i]:
                flag += 0                           # flag does not change
                new_box += answer[i]                # new_box store player guess temporarily
            elif input_ch != answer[i]:
                if old_box[i] != '-':
                    new_box += old_box[i]           # old_box store player guess answer
                else:
                    new_box += '-'
        if old_box != new_box:                      # if guess right
            print('You are correct!')
            print('The word looks like: ', end='')
        if old_box == new_box:
            if old_box.find(input_ch) != -1:        # if guess right for same character again
                flag += 0
                print('You are correct!')
                print('The word looks like: ', end='')
            else:                                   # if guess wrong
                flag += 1
                print('There is no ' + str(input_ch) + "'s in the word.")
                if N_TURNS == flag:                 # terminal condition
                    extension(flag)
                    print("You are completely hung : (")
                    print('The word was: ', end='')
                    print(answer)
                    break
                else:
                    print('The word looks like: ', end='')
        print(new_box, end='')
        old_box = new_box
        new_box = ''
        if answer == old_box:                       # terminal condition
           print("\nYou win !!")
           print('The word was: ', end='')
           print(answer)
           break
        print("")                                   # make a new line
        print('You have ' + str(int(N_TURNS) - flag) + ' guesses left.')
        extension(flag)                             # print image
        input_ch = input('Your guess:')
        while not input_ch.isalpha() or len(input_ch) != 1:
            print('illegal format.')               # if input non-alphabet or more than one character,input again.
            input_ch = input('Your guess:')
        input_ch = input_ch.upper()


"""
This function is to print hangman image.
"""
def extension(f):
    print('------')
    if f == 0:
        for i in range(6):
            print('|')
    elif f == 1:
        print('|     |')
    elif f == 2:
        print('|     |')
        print('|   -----')
    elif f == 3:
        print('|     |')
        print('|   -----')
        print('|   |. .|')
    elif f == 4:
        print('|     |')
        print('|   -----')
        print('|   |. .|')
        print('|   -----')
        print('|     |')
    elif f == 5:
        print('|     |')
        print('|   -----')
        print('|   |. .|')
        print('|   -----')
        print('|     |')
        print('|   \\ | /')
        print('|    \\|/')
    elif f == 6:
        print('|     |')
        print('|   -----')
        print('|   |. .|')
        print('|   -----')
        print('|     |')
        print('|   \\ | /')
        print('|    \\|/')
        print('|     |')
        print('|     |')
    elif f == 7:
        print('|     |')
        print('|   -----')
        print('|   |. .|')
        print('|   -----')
        print('|     |')
        print('|   \\ | /')
        print('|    \\|/')
        print('|     |')
        print('|     |')
        print('|    / \\')
        print('|   /   \\')
    print('---')
    


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
