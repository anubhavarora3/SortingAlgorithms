def insertionSort(arr):
	n = len(arr)

	for i in range(1, n):
		value = arr[i]
		hole = i

		while hole > 0  and arr[hole-1] > value:
			arr[hole] = arr[hole-1]
			hole = hole -1

		arr[hole] = value

arr = [64, 34, 25, 12, 22, 11, 90]

insertionSort(arr)

print("The sorted array is:")
for i in range(len(arr)):
	print(arr[i], end = ', ')
print('\n')