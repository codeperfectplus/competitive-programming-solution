

def maxTotalRectangleArea(arr):
	arr.sort(reverse=True)

	n = len(arr)
	sum = 0
	flag = False

	length = 0
	i = 0

	while (i < n-1):
		if (i != 0):
			i = i + 1
	
		if ((arr[i] == arr[i+1] or arr[i] - arr[i+1] ==1) and flag==False):
			flag = True
			length = arr[i + 1]

			i = i + 1

		elif ((arr[i] == arr[i+1] or arr[i] - arr[i+1] ==1) and flag==True):
			sum = sum + arr[i +1] * length

			flag = False

			i = i + 1

	return sum

a = [ 10, 10, 10, 10, 11, 10, 11, 10, 9, 9, 8, 8 ]

print(maxTotalRectangleArea(a))
