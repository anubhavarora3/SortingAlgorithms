def selectionSort(arr):
	n = len(arr)

	for i in range(n-1):
		iMin = i
		for j in range(i+1, n):
			if arr[j] < arr[iMin]:
				iMin = j
		arr[i], arr[iMin] = arr[iMin], arr[i]


arr = [64, 34, 25, 12, 22, 11, 90]

selectionSort(arr)

print("The sorted array is:")
for i in range(len(arr)):
	print(arr[i], end = ', ')
print('\n')