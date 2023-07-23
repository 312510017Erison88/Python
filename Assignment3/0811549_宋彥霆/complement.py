"""
File: complement.py
Name:0811549 宋彥霆
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    To find the complement of original DNA
    """
    dna = input("Please give me a DNA strand and I'll find the complement:")
    dna = dna.upper()                   # make case-insensitive
    new_dna = build_complement(dna)
    print('The complement of '+str(dna)+' is '+str(new_dna))


def build_complement(dna):
    ans = ""
    for i in range(len(dna)):           # This for loop is to complete 'A''T''C''G' base respectively
        base = dna[i]
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        else:
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
