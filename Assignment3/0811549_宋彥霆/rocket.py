"""
File: rocket.py
Name: 0811549 宋彥霆
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 6


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):					# print the row
		for j in range(SIZE-i):				# print space
			print(' ', end='')
		for j in range(i+1):				# print /
			print('/', end='')
		for j in range(i+1):				# print \
			print('\\', end='')
		print('')							# make to new line


def belt():
	print('+', end='')						# print first +
	for i in range(SIZE*2):					# print =
		print('=', end='')
	print('+', end='')						# print second +
	print('')								# make to new line


def upper():
	for i in range(SIZE):
		print('|', end='')					# print |
		for j in range(SIZE-i-1):
			print('.', end='')				# print .
		for j in range(i+1):
			print('/\\', end='')			# print /\
		for j in range(SIZE-i-1):
			print('.', end='')
		print('|', end='')
		print('')


def lower():
	for i in range(SIZE):
		print('|', end='')					# print |
		for j in range(i):
			print('.', end='')				# print .
		for j in range(SIZE-i):
			print('\\/', end='')			# print \/
		for j in range(i):
			print('.', end='')
		print('|', end='')
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	#print("123")
	main()