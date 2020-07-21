user = int(input("Enter number here: "))



def one(user):
	number = user
	if number % 4 == 0:
		two(number)

	else:
		five(number)

def two(number):
	num = number
	if num % 100 == 0:
		three(num)

	else:
		four(num)


def three(num):
	year = num

	if year % 400 == 0:
		four(year)

	else:
		five(year)


def four(year):
	print("True")


def five(num):
	print("False")


one(user)

