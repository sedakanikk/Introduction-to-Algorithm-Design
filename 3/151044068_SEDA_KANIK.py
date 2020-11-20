################################################## ANSWER OF 3TH QUESTION ##################################################

# insertion sort
# calculates number of swap operations
# in fact insertion sort do not have any swap operations but i assume that, every displacement and shifting operations are swap
def iSort3(arr):
	swap = 0
	length = len(arr)
	for nextIndex in range(1, length):
		swap += insert3(arr, nextIndex)
	return swap

# inserts and shifts all the other elements if necessary
def insert3(arr, nextIndex):
	nextValue = arr[nextIndex]
	swap = 0;
	while(nextIndex>0 and nextValue<arr[nextIndex-1]):
		arr[nextIndex] = arr[nextIndex-1]
		swap += 1
		nextIndex -= 1
	arr[nextIndex] = nextValue
	return swap

# quick sort
# calculates number of swap operations
def qSort3(arr):
	swap = 0
	swap = quickSort3(arr, 0, len(arr)-1, swap)
	return swap

# selects a pivot, first and last values, then compares these three values
# swaps first and last values if first value is bigger than and last value is smaller than pivot, then selects new first and last values then repeats again
# if first and last elements are in the same location or first's location is bigger than lasts', then selects new pivot and repeats these operations again  
def quickSort3(arr, firstIndex, lastIndex, swap):
	if(firstIndex < lastIndex):
		pivotIndex, swap2 = partition3(arr, firstIndex, lastIndex, swap)
		swap3 = 0
		swap += quickSort3(arr, firstIndex, pivotIndex-1, swap3)
		swap += quickSort3(arr, pivotIndex+1, lastIndex, swap3)
		swap += swap2
	return swap

def partition3(arr, first, last, swap):
	pivot = arr[first]
	copyFirstIndex = first
	copyLastIndex = last
	while True:
		while( (copyFirstIndex<last) and (pivot>=arr[copyFirstIndex]) ):
			copyFirstIndex += 1
		while( pivot<arr[copyLastIndex] ):
			copyLastIndex -= 1
		if(copyFirstIndex<copyLastIndex):
			swap += swapFunc3(arr, copyFirstIndex, copyLastIndex)
		if(copyFirstIndex>=copyLastIndex):
			break
	swap += swapFunc3(arr, first, copyLastIndex)
	return copyLastIndex, swap

# literally swaps two values
def swapFunc3(arr, index1, index2):
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp
	return 1

################################################## ANSWER OF 4TH QUESTION ##################################################
# finds median using quick sort
# first takes a list or an array then sort it using quick sort and finds the median 
def quickSort4(arr, firstIndex, lastIndex):
	if(firstIndex < lastIndex):
		pivotIndex = partition4(arr, firstIndex, lastIndex)
		quickSort4(arr, firstIndex, pivotIndex)
		quickSort4(arr, pivotIndex+1, lastIndex)

def partition4(arr, first, last):
	pivotElement = arr[first]
	i = first-1
	j = last+1

	while True:
		while True:
			i += 1
			if(arr[i]>=pivotElement):
				break
		while True:
			j -= 1
			if(arr[j]<=pivotElement):
				break
		if (i>=j):
			return j
		swapFunc4(arr, i, j)

# literally swaps two values
def swapFunc4(arr, index1, index2):
	temp = arr[index1]
	arr[index1] = arr[index2]
	arr[index2] = temp
	return 1

# finds the median
def findMedian(arr):
	median = arr[(int)(len(arr)/2)]
	return median

################################################## ANSWER OF 5TH QUESTION ##################################################
# finds all subarrays recursively
# first recursive call increases index and calculates subarrays,
# second recursive call increases index and get together elements of array to make subarray
def findSubarrays(arr, index, sub, res):
	if(index == len(arr)):
		if(len(sub) != 0):
			res.insert(len(res), sub)
	else:
		findSubarrays(arr, index+1, sub, res)
		findSubarrays(arr, index+1, sub+[arr[index]], res)
	return

# finds sum of all elements of subarrays recursively 
# checks if out of range or not for given array 
# if not, adds element with previous elements of subarray and if subarray ends, inserts this value in arrSum array and makes recursive call
def findSumofSub(arr, arrSum, Findex, Sindex, temp):
	if(Findex == len(arr)):
		return arrSum
	else:
		if(Sindex<len(arr[Findex])):
			temp += arr[Findex][Sindex]
			return findSumofSub(arr, arrSum, Findex, Sindex+1, temp)
		else:
			arrSum.insert(len(arrSum), temp)
			temp = 0
			return findSumofSub(arr, arrSum, Findex+1, 0, temp)

# finds mult of all elements of subarrays recursively 
# checks if out of range or not for given array 
# if not, mults element with previous elements of subarray and if subarray ends, inserts this value in arrMult array and makes recursive call
def findMultofSub(arr, arrMult, Findex, Sindex, temp):
	if(Findex == len(arr)):
		return arrMult
	else:
		if(Sindex<len(arr[Findex])):
			temp *= arr[Findex][Sindex]
			return findMultofSub(arr, arrMult, Findex, Sindex+1, temp)
		else:
			arrMult.insert(len(arrMult), temp)
			temp = 1
			return findMultofSub(arr, arrMult, Findex+1, 0, temp)

# finds the optimal subarray for solution recursively
# takes all the calculated values and arrays, and uses all the parameter
# if there is no out of range, then, 
# if identified value of given sum array is bigger than result for array, then look their multiplication result to select optimal subarray
def findsOptimalSubarray(arrSum, resforArr, index, res, resIndex, arrMult):
	if(index == len(arrSum)):
		return resIndex
	else:
		if( (1.0*arrSum[index])<=resforArr and (1.0*res)<=resforArr and res<arrSum[index] and arrMult[resIndex]<arrMult[index]):
			res = arrSum[index]
			resIndex = index
		elif( (1.0*arrSum[index])<=resforArr and (1.0*res)<=resforArr and res>arrSum[index] and arrMult[resIndex]>arrMult[index]):
			res = res
			resIndex = resIndex
		elif((1.0*arrSum[index])>=resforArr and (1.0*res)>=resforArr and res>arrSum[index] and arrMult[resIndex]>arrMult[index]):
			res = arrSum[index]
			resIndex = index
		elif((1.0*arrSum[index])>=resforArr and (1.0*res)>=resforArr and res<arrSum[index] and arrMult[resIndex]<arrMult[index]):
			resIndex = resIndex
		elif((1.0*arrSum[index])>=resforArr and (1.0*res)<=resforArr):
			res = arrSum[index]
			resIndex = index
		elif((1.0*arrSum[index])<=resforArr and (1.0*res)>=resforArr):
			resIndex = resIndex
		return findsOptimalSubarray(arrSum, resforArr, index+1, res, resIndex, arrMult)

# driver function for call all the functions
def main():
	print("********************QUESTION3********************")
	arr1 = [2, 5, 3, 4, 9, 4, 15, 6, 2, 0]
	arr2 = [2, 5, 3, 4, 9, 4, 15, 6, 2, 0]
	print ("Before Sorting : ")
	print ("array for insertion sort: ")
	print (arr1)
	print ("array for quick sort: ")
	print (arr2)
	print ("**************************************")
	swap1 = iSort3(arr1)
	swap2 = qSort3(arr2)
	print ("After Insertion Sort : ")
	print (arr1)
	print ("Count of swap for insertion sort: ")
	print (swap1)
	print ("**************************************")
	print ("After Quick Sort : ")
	print (arr2)
	print ("Count of swap for quick sort: ")
	print (swap2)

	print("********************QUESTION4********************")
	arr3 = [10, 7, 9, 8, 17, 13, 4, 5, 3, 6, 0]
	length = len(arr3)
	print("Before sorted:")
	print (arr3)
	quickSort4(arr3, 0, length-1)
	print("After sorted:")
	print (arr3)
	median = findMedian(arr3)
	print("Median is: ")
	print(median)

	print("********************QUESTION5********************")
	# defined an array to use in all the functions
	arr = [2,4,7,5,22,11]
	print("Array is: ")
	print(arr)
	subarrays = []
	temparr = []
	
	arr.sort(reverse = True)
	findSubarrays(arr, 0, temparr, subarrays)
	print("All subarrays: ")
	print(subarrays)
	maxofarr = max(arr)
	minofarr = min(arr)
	resforArr = 1.0*(maxofarr+minofarr)*len(arr)/4.0

	arrSum =[]
	arrSum = findSumofSub(subarrays, arrSum, 0, 0, 0)

	arrMult = []
	arrMult = findMultofSub(subarrays, arrMult, 0, 0, 1)

	res = arrSum[0]
	index = findsOptimalSubarray(arrSum, 1.0*resforArr, 1, res, 0, arrMult)
	print("Optimal subarray: ")
	print(subarrays[index])

# calls driver program
main()