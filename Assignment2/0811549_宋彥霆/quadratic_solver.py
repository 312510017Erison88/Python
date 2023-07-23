"""
File: quadratic_solver.py
Name:0811549  宋彥霆
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math

def main():
	"""
	To create the quadratic solver
	"""
	print('stanCode Quadratic Solver!')
	a = float(input('Please input an number for a:'))					#input a, and a can be float
	if a == 0:
		a = float(input('Please input an number for a again.'))		# let a!=0
	b = float(input('Please input an number for b:'))					#input b, and a can be float
	c = float(input('Please input an number for c:'))					#input c, and a can be float
	if (b**2-4*a*c) < 0:
		print('No real roots')
	else:
		x = (-b+math.sqrt(b**2-4*a*c))/2*a		# one of the root for equation
		y = (-b-math.sqrt(b**2-4*a*c))/2*a		# another root for equation
		if (b**2-4*a*c) > 0:						# two different root condition
			print('Two roots: '+str(x)+' , '+str(y))
		elif (b**2-4*a*c) == 0:					# one root condition
			print('One root: '+str(x))

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
