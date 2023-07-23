"""
File: similarity.py
Name:0811549  宋彥霆
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    To compare the two sequence's similarity, and print the best match sequence.
    """
    long = input("Please give me a DNA sequence to search: ")
    long = long.upper()
    short = input("What DNA sequence would you like to match?")
    short = short.upper()

    """
    This for loop is to compare the number of same alphabet between long string 
    and short string, and find the max number which location is the start  
    """
    flag = 0
    similarity = 0
    for i in range(len(long) - len(short) + 1):
        total = 0
        for j in range(len(short)):
            if long[i+j] == short[j]:
                total += 1                      # jog down the number of same alphabet in total.
        if total > similarity:                  # make similarity store the max value
            similarity = total
            flag = i                            # print start from flag
    print("The best match is ", end='')
    for i in range(len(short)):                 # print the best match
        print(str(long[flag+i]), end='')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
