# comments and explanations of functions are in report file
"""******************************************************************* ANSWER 1 - B *******************************************************************"""

def check_array(arr, m, n, difference):

	newArr = []
	for i in range(0, m-2):
		for j in range(0, n-2):
			if( (arr[i][j] + arr[i+1][j+1]) > (arr[i][j+1] + arr[i+1][j]) ):
				newArr.append(i)
				newArr.append(i+1)
				newArr.append(j)
				newArr.append(j+1)
				difference.append((arr[i][j] + arr[i+1][j+1]) - (arr[i][j+1] + arr[i+1][j]))

	return newArr

def change_array(arr, subarray, difference):
	length = len(subarray)
	temp = 0 
	while(difference != []):
		for i in range(0, length, 4):
			diff = difference[int(i/4)]
			if(temp == 0):
				arr[subarray[i+1]][subarray[i+2]] += diff # i+1 j
				temp = 1
			elif(temp == 1):
				arr[subarray[i]][subarray[i+3]] += diff # i j+1
				temp = 2
			elif(temp == 2):
				arr[subarray[i]][subarray[i+2]] -= diff # i j
				temp = 3
			elif(temp == 3):
				arr[subarray[i+1]][subarray[i+3]] -= diff # i+1 j+1
				temp = 0

			difference = []
			last = check_array(arr, len(arr), len(arr[0]), difference)

			if difference: 
				if(temp == 0):
					arr[subarray[i+1]][subarray[i+3]] += diff
				elif(temp == 1):
					arr[subarray[i+1]][subarray[i+2]] -= diff
				elif(temp == 2):
					arr[subarray[i]][subarray[i+3]] -= diff
				elif(temp == 3):
					arr[subarray[i]][subarray[i+2]] += diff
			if not difference:
				break; 
			difference.pop(0)
			last = check_array(arr, len(arr), len(arr[0]), difference)

"""******************************************************************* ANSWER 1 - C *******************************************************************"""

def find_leftmost(arr, leftmin):

	leftMin = 0
	for i in range(0, len(arr)):
		min_element = arr[i][0] 
		for j in range(0, len(arr[i])):
			# If found new minimum  
			if (arr[i][j] < min_element):
				leftMin = j
				min_element = arr[i][j]
		leftmin.append(min_element)

def find_leftmost_minelement(arr, leftmin):
	mid = int(len(arr)/2)
	find_leftmost(arr[:mid], leftmin)
	find_leftmost(arr[mid:], leftmin)

"""******************************************************************* ANSWER 2 *******************************************************************"""

def kthlargest(arr1, arr2, k):
	if( len(arr1) + len(arr2) < k):
		print ("Total size of A and B arrays is not enough for", k+1, "th element")
		return None
	elif(k < 0):
		print ("The", k+1, "th element is impossible")
		return None
	elif ( len(arr1) == 0):
		return arr2[k]
	elif ( len(arr2) == 0 ):
		return arr1[k]

	mid1 = int(len(arr1)/2)
	mid2 = int(len(arr2)/2)
	
	if (mid1+mid2 < k):
		if (arr1[mid1]>arr2[mid2]):
			return kthlargest(arr1, arr2[mid2+1:], k-(mid2+1))
		else:
			return kthlargest(arr1[mid1+1:], arr2, k-(mid1+1))
	else:
		if (arr1[mid1]>arr2[mid2]):
			return kthlargest(arr1[:mid1], arr2, k)
		else:
			return kthlargest(arr1, arr2[:mid2], k)

"""******************************************************************* ANSWER 3 *******************************************************************"""

def calculate_sums(arr, findex, mindex, lindex):

	sumofelements = 0

	first_sum = -99999
	for i in range(mindex, findex, -1):
		sumofelements = sumofelements + arr[i]

		if (sumofelements > first_sum):
			first_sum = sumofelements

	# Include elements on right of mid 
	sumofelements = 0

	last_sum = -99999
	for i in range(mindex+1, lindex + 1):
		sumofelements = sumofelements + arr[i]

		if (sumofelements > last_sum):
			last_sum = sumofelements

	return first_sum + last_sum


def maxsum_subarray(arr, findex, lindex):

	if (findex == lindex):
		return arr[findex]

	# Find middle point
	mindex = int((findex + lindex)/2)
	left = maxsum_subarray(arr, findex, mindex)
	right = maxsum_subarray(arr, mindex+1, lindex)
	sums = calculate_sums(arr, findex, mindex, lindex)	

	if(left>right and left>sums):
		res = left
	elif(right>left and right>sums):
		res = right
	else:
		res = sums
	return res

def find_array(arr, res):

	for i in range(0, len(arr)):
		temp = []
		sums = 0
		for j in range (i,len(arr)):
			sums += arr[j]
			temp.append(arr[j])
			if(sums == res):
				return temp

"""******************************************************************* ANSWER 4 *******************************************************************"""

def isBipartite(arr, vertex_number):
	colored = [-1] * vertex_number
	colored[0] += 2
	temp = []
	temp.append(0)

	while (temp != []):
		index = temp.pop()

		if(arr[index][index] == 1):
			return False
		stage = coloring(arr[index], index, colored, temp, vertex_number)
		if(stage == False):
			return False
	return True

def coloring(arr, index, colored, temp, vertex_number):
	for i in range (0, vertex_number):
		if(arr[i] == 1 and colored[i] == -1):
			if(colored[index] == 0):
				colored[i] = 1
			elif(colored[index] == 1):
				colored[i] = 0

			temp.append(i)

		elif(arr[i] == 1 and colored[i] == colored[index]):
			return False

"""******************************************************************* ANSWER 5 *******************************************************************"""

def bestday(arr_cost, arr_price, arr_gain, bestday_index):

	for i in range (len(arr_cost)):
		gain = arr_price[i]-arr_cost[i]
		if(gain <= 0):
			print (i+1,"th day could not make money.")
		arr_gain.append(gain)
	
	for i in range (len(arr_gain)):
		if(arr_gain[bestday_index]<arr_gain[i]):
			bestday_index = i
	return bestday_index

def calculate_bestday(arr_cost, arr_price, arr_gain, bestday_index):

	mid_cost = int(len(arr_cost)/2)
	if(mid_cost == 0):
		print("There is no day to make money.")
		return -1
	mid_price = int(len(arr_price)/2)
	arr_gain.append(0)
	bestday_index = bestday(arr_cost[:mid_cost], arr_price[1:mid_price+1], arr_gain, bestday_index)
	bestday_index = bestday(arr_cost[mid_cost:len(arr_cost)-1], arr_price[mid_price+1:], arr_gain, bestday_index)
	return bestday_index

def main():

	"""******************************************************************* ANSWER 1 - B *******************************************************************"""
	print ("******************************** ANSWER 1 - B ********************************")
	print ("********************************************************")
	arr = [[37, 23, 22, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]
	difference = []
	last = check_array(arr, len(arr), len(arr[0]), difference)
	change_array(arr, last, difference)
	print ("arr: ", arr)
	
	print ("********************************************************")
	arr = [[37, 23, 24, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]
	difference = []
	last = check_array(arr, len(arr), len(arr[0]), difference)
	change_array(arr, last, difference)
	print ("arr: ", arr)

	"""******************************************************************* ANSWER 1 - C *******************************************************************"""
	print ("******************************** ANSWER 1 - C ********************************")
	print ("********************************************************")
	arr = [[37, 23, 22, 32], [21, 6, 7, 10], [53, 34, 30, 31], [32, 13, 9, 6], [43, 21, 15, 8]]
	leftmin = []
	find_leftmost_minelement(arr, leftmin)
	print ("leftmin elements : ", leftmin)
	
	print ("********************************************************")
	arr = [[26,48,15,98,67,22], [34,68,10,69,52,43], [72,64,39,28,55,46], [32,13,32,64,49,71], [16,19,17,12,11,62]]
	leftmin = []
	find_leftmost_minelement(arr, leftmin)
	print ("leftmin elements : ", leftmin)

	"""******************************************************************* ANSWER 2 *******************************************************************"""
	print ("******************************** ANSWER 2 ********************************")
	print ("********************************************************")
	arr1 = [1,4,7,8,12,15]
	arr2 = [3,5,6,9,11,13,14]
	k=10
	p = kthlargest(arr1, arr2, k-1)
	print (p)
	
	print ("********************************************************")
	arr1 = [5,12,19]
	arr2 = [3,4,6,11,23,24,29,30,35]
	k=4
	p = kthlargest(arr1, arr2, k-1)
	print (p)
	
	print ("********************************************************")
	arr1 = [5,12,19]
	arr2 = [3,4,6,11,23,24,29,30,35]
	k=40
	p = kthlargest(arr1, arr2, k-1)
	print (p)

	"""******************************************************************* ANSWER 3 *******************************************************************"""
	print ("******************************** ANSWER 3 ********************************")
	print ("********************************************************")
	arr = [5, -6, 6, 7, -6, 7, -4, 3]
	n = len(arr) 
	max_sum = maxsum_subarray(arr, 0, n-1) 
	subarray = find_array(arr, max_sum)
	print ("subarray is:",subarray)
	print("Maximum contiguous sum is ", max_sum) 

	print ("********************************************************")
	arr = [5, -6, 6, 7, -6, 7, 10,-3, 4, -4, 3]
	n = len(arr) 
	max_sum = maxsum_subarray(arr, 0, n-1) 
	subarray = find_array(arr, max_sum)
	print ("subarray is:",subarray)
	print("Maximum contiguous sum is ", max_sum)

	"""******************************************************************* ANSWER 4 *******************************************************************"""
	print ("******************************** ANSWER 4 ********************************")
	print ("********************************************************")
	arr = [[0,1], [1,0]] # example of bipartite
	print (isBipartite(arr, len(arr)))

	print ("********************************************************")
	arr = [[0,1,1], [1,0,1], [1,1,0]] # example of not bipartite
	print (isBipartite(arr, len(arr)))

	print ("********************************************************")
	arr = [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]] # example of bipartite
	print (isBipartite(arr, len(arr)))

	print ("********************************************************")
	arr = [[0,1,0,0,1], [1,0,1,0,0], [0,1,0,1,0], [0,0,1,0,1], [1,0,0,1,0]] # example of not bipartite
	print (isBipartite(arr, len(arr)))

	print ("********************************************************")
	arr = [[0,1,0,0,0,1], [1,0,1,0,0,0], [0,1,0,1,0,0], [0,0,1,0,1,0], [0,0,0,1,0,1], [1,0,0,0,1,0]] # example of bipartite
	print (isBipartite(arr, len(arr)))
	
	"""******************************************************************* ANSWER 5 *******************************************************************"""
	print ("******************************** ANSWER 5 ********************************")
	print ("********************************************************")
	arr_cost = [5,11,2,21,5,7,8,12,13,None]
	arr_price = [None,7,9,5,21,7,13,10,14,20]
	arr_gain = []
	bestday_index = 0
	bestday_index = calculate_bestday(arr_cost, arr_price, arr_gain, bestday_index)
	if(bestday_index != -1):
		print ("The best day to buy goods is the",bestday_index,"th days,")
		print ("sell them on the",bestday_index+1,"th day,")
		print ("you can make", arr_gain[bestday_index],"units of money, which is the maximum possible gain in the schedule.")

	print ("********************************************************")
	arr_cost = [12,4,8,31,50,4,6,9,7,None]
	arr_price = [None,12,15,16,41,27,15,3,4,7]
	arr_gain = []
	bestday_index = 0
	bestday_index = calculate_bestday(arr_cost, arr_price, arr_gain, bestday_index)
	if(bestday_index != -1):
		print ("The best day to buy goods is the",bestday_index,"th days,")
		print ("sell them on the",bestday_index+1,"th day,")
		print ("you can make", arr_gain[bestday_index],"units of money, which is the maximum possible gain in the schedule.")

	print ("********************************************************")
	arr_cost = [5]
	arr_price = [None]
	arr_gain = []
	bestday_index = 0
	bestday_index = calculate_bestday(arr_cost, arr_price, arr_gain, bestday_index)
	if(bestday_index != -1):
		print ("The best day to buy goods is the",bestday_index,"th days,")
		print ("sell them on the",bestday_index+1,"th day,")
		print ("you can make", arr_gain[bestday_index],"units of money, which is the maximum possible gain in the schedule.")
	

main()