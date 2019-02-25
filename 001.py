def mult35():
	count = 0
	for i in range(0,10):
		if (i%3 == 0):
			count += i
			i += 1
		elif(i%5 == 0):
			count += i
			i += 1
		else:
			i += 1
	print(count)

mult35()
