count = 0
degrees = []

while count < 3:
	correct = True
	while correct:
		try:
			user_input = int(input("Enter an angle of the triangle: "))
			degrees.append(user_input)
			correct = False
			count = count + 1

		except:
			correct = True


summation = sum(degrees)

if summation == 180:
	print("An ideal triangle")

	if degrees[0] == 90 or degrees[1] == 90 or degrees[2] == 90:
		print("A right angles triangle")

else:
	print("This is not even a triangle ")


