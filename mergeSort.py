import math
def Merge(L, R , arr):
	nL = len(L)
	nR = len(R)

	i, j, k = 0, 0, 0

	while i < nL and j < nR:
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < nL:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < nR:
		arr[k] = R[j]
		j += 1
		k += 1

def MergeSort(arr):
	n = len(arr)

	if n < 2:
		return arr

	mid = math.ceil(n/2) 
	#temp arrays
	L = [0] * mid
	R = [0] * (n-mid)

	for i in range(mid):
		L[i] = arr[i]

	for j in range(mid, n):
		R[j - mid] = arr[j] 

	MergeSort(L)
	MergeSort(R)
	Merge(L, R, arr)

arr = [64, 34, 25, 12, 20, 11, 90]

MergeSort(arr)

print("The sorted array is:")
for i in range(len(arr)):
	print(arr[i], end = ', ')
print('\n')