"""
File: hailstone.py
Name:0811549  宋彥霆
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

def main():
    """
    To finish the hailstone equation
    """
    print('This program computes Hailstone sequences.\n')
    x = float(input('Enter a number: '))
    while x != int(x):        # To prevent user to input float!
        print('Please input an integer again!')
        x = float(input('Enter a number: '))
    flag = 0                  # To calculate how many step to take
    while x != 1:
        if (x%2 == 1):        # if x is odd number
            x = 3*x+1
            print(str(int((x-1)/3)) +' is odd, so I make 3n+1: '+str(int(x)))
            flag += 1
        else:               # if x is even number
            x=x/2
            print(str(int(x*2)) + ' is even, so I take half: ' +str(int(x)))
            flag += 1
    print('It took '+str(flag)+' steps to reach 1.')

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
