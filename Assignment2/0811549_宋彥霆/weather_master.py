"""
File: weather_master.py
Name:0811549  宋彥霆
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT=-100			# make exit be a constant
CLOD_DAY=16			# make exit be a constant
def main():
	"""
	To find highest temp, lowest temp, average temp, how many cold days
	"""
	print('standCode "Weather Master 4.0"!')
	cold_days = 0
	highest_temp = -10000000
	lowest_temp = 100000000
	"""
	Users first input 
	"""
	a = int(input('Next Temperature: (or '+str(EXIT)+' to quit)?'))
	if a != EXIT:
		if a < CLOD_DAY:			# To calculate how many cold days.
			cold_days = 1
		if a > highest_temp:  		# To let first input be the maximum temperature temperately.
			highest_temp = a
		if a < lowest_temp:  		# To let first input be the minimum temperature temperately.
			lowest_temp = a
		total = a
		flag = 1					# how many times you input
		"""
		Users others inputs
		"""
		while a != EXIT:
			a = int(input('Next Temperature: (or '+str(EXIT)+' to quit)?'))
			if a != EXIT:
				total += a					# calculate the total of all temperature
				flag += 1					# calculate how many times you input
				if a > highest_temp:		# To find the max temperature.
					highest_temp = a
				if a < lowest_temp:			# To find the min temperature.
					lowest_temp = a
				if a < CLOD_DAY:
					cold_days += 1			# To calculate how many cold days.
			else:
				break
		average = total/flag				# To calculate the average temperature.

		print('Highest temperature = ', highest_temp)
		print('Lowest temperature = ', lowest_temp)
		print('Average = ', average)
		print(str(cold_days)+' cold day(s)')
	else:
		print('No temperatures were entered.')		#if user want to leave at first time

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
