def isbnCheck():
	b = ''
	count = 0
	while count < 3:

		user = input("Enter ISBN number with or without hyphens: ")

		data = user.split('-')

		for i in data:
			b = b + str(i)

		print(b)

		if len(b) != 10:
			print("Invalid input")
			b = ''
			count = count + 1

		else:
			ind = b[-1]

			data = b[0:9]

			numbers = data

			try:
				print("Here", numbers)
				number = int(numbers)
				print(number)

				if b[-1] == 'X' or b[-1] == 'x':
					last_digit = 10
					print(last_digit)

					all_numbers = str(number) + str(last_digit)
					print(all_numbers)

					all_number = calculate(all_numbers)
					count = 4

				else:
					try:
						last_digit = int(b[-1])
						print(last_digit)

						all_numbers = str(number) + str(last_digit)
						print("Heeee", all_numbers)

						all_number = calculate(all_numbers)
						count = 4

					except:
						print("invalid check code")
						b = ''
						count = count + 1


			except:
				print("Invalid int input")
				b = ''
				count = count + 1




def calculate(numbers):
	mul = 10
	biglist = []
	all_numbers = numbers
	print("cal", all_numbers)

	for num in all_numbers[0:9]:
		print(num)
		number = int(num)
		mulli = number * mul
		biglist.append(mulli)
		mul = mul - 1

	last_digit = int(all_numbers[9:])

	biglist.append(last_digit*mul)

	print(biglist)

	total = sum(biglist)
	print(total)

	if total % 11 == 0:
		print("A valid ISBN number")
	else:
		print("Invalid ISBN number")

	return total




isbnCheck()