
def divide(array):

	n = len(array)

	left = array[:n//2]
	right = array[n//2:]

	if len(left) <= 1 or len(right) <= 1:
		return merge(left, right)
	else:
		left = divide(left)
		right = divide(right)
		return merge(left, right)

	

def merge(array1, array2):

	n = len(array1) + len(array2)

	maximun = 0
	if max(array1) >= max(array2):
		maximun = max(array1)
	else:
		maximun = max(array2)

	array1.append(maximun+1)
	array2.append(maximun+1)
 
	sorted_array = []

	i = 0
	j = 0

	for k in range(0, n):

		if array1[i] >= array2[j]:
			sorted_array.append(array2[j]) 
			j += 1
		elif array1[i] < array2[j]:
			sorted_array.append(array1[i])
			i += 1

	return sorted_array



