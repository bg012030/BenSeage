number = [9 , 7 , 5 , 3 , 1]
for i in range(len(number)-1,0,-1):
	for n in range(0,i):
		if  number[n] > number[n+1]:
			a = number[n+1]
			number[n+1] = number[n]
			number[n] = a
			
	  
