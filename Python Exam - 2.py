# Python Exam exercise 2

def main ():
	number = check_input()
	result = count_random(number)
	answer = check_if_prime(result)
	print("Number", result, answer)

# -------------------------------------------------------------

def check_input():
	number_tested = 0
	valid_number = 0
	while valid_number == 0:

		number_tested = int(input('Give a number between 10-30 or 45-50: '))

		if (number_tested >= 10 and number_tested <=30) or (number_tested >=45 and number_tested <=50) :
			valid_number = 1
		else:
			print("Try again, this number is not valid")
			valid_number =0

	return number_tested

# -------------------------------------------------------------

def count_random(dividend):
	import random as random
	random_number = int(round(random.uniform(20, 999)))
	division = int(round(random_number / dividend))
	return division

# -------------------------------------------------------------

def check_if_prime(my_number):
	if my_number > 1:
		for n in range(2, my_number):
			if(my_number % n) == 0:
				return (f'{my_number} is not a prime number')
			else:
				return (f'{my_number} is a prime number')

main()