def quickSort(list):
	length = len(list)

	if(length == 1):
		return list
	elif(length == 2):
		if(list[0] > list[1]):
			swap(list,0,1)
		return list

	a = 0
	b = length-2
	pivot = list[length-1]
	while(a<b):
		print("a:{0} b:{1} pivot:{2} | {3}".format(a,b,pivot,list))
		if(list[a] <= pivot):
			a = a + 1
		if(list[b] > pivot):
			b = b - 1
		if(list[a] > pivot & list[b] < pivot):
			swap(list,a,b)
			print("Swapped a and b")
	swap(list,len(list)-1,a)
	print("swapped pviot {0}".format(list))
	return [quickSort(list[0:a-1]),list[a],quickSort(list[a+1:b])]

    
def swap(array, index1, index2):
	temp = array[index1]
	array[index1] = array[index2]
	array[index2] = temp


