number1 = []
while True:
	try:
		number = input("enter a number or Enter to finish: ")
		if number:
			number1.append(int(number))
		else:
			break
	except ValueError as error:
		print(error)

print ("number : " , number1)
print ("count = " , len(number1))
print ("sum = " , sum(number1))
print ("lowest = " , min(number1))
print ("highest = " , max(number1))
print ("mean = " , sum(number1) / len(number1))

		