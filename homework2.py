import random
name = ["man" , "woman" , "dog" , "cat"]
adv = ["loudly" , "quietly" , "well" , "badly"]
v = [ "jumped" , "hoped" , "laughed" ]
a = ["the" , "a"]
while True:
	try:
		number = input("Please number of times(1-10)")
		if not 0 < int(number) < 11:
			continue
		else:
			break
	except ValueError as error:
		print(error)

for i in range(0,int(number)):
	if random.randint(0,1) == 0:
		print(random.choice(a) , random.choice(name) , random.choice(v) , random.choice(adv))
	else:
		print(random.choice(a) , random.choice(name) , random.choice(v))
	