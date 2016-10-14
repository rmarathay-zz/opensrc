def binarySearch(input, value):
	temp = sorted(input);
	print(temp)
	index = len(input)+1/2
	if(value == input[index]):
		print "found", value
	elif(value > input[index]):
		binarySearch(temp[index:],value)
	elif(value < input[index]):
		binarySearch(temp[:index],value)
	elif(index == 0):
		print "Does not exist in input"


list = [1,3,4,6,7,8,9]

binarySearch(list, 10);