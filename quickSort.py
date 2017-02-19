def quickSort(arr, start, end):
	if start >= end:
		return

	pIndex = partition(arr, start, end)
	quickSort(arr, start, pIndex-1)
	quickSort(arr, pIndex+1 , end)

def partition(arr, start, end):
	pivot = arr[end]
	pIndex = start

	for i in range(start,end):
		if arr[i] < pivot:
			arr[i], arr[pIndex] = arr[pIndex], arr[i]
			pIndex += 1

	arr[pIndex], arr[end] = arr[end], arr[pIndex]
	return pIndex


arr = [64, 34, 25, 12, 20, 11, 90]
n = len(arr)
quickSort(arr,0, n-1)

print("The sorted array is:")
for i in range(len(arr)):
	print(arr[i], end = ', ')
print('\n')