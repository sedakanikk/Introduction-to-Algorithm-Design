"""**************************************** ANSWER - 1 ****************************************"""
"""
-calculates two option and selects one of them at the end
-sums with the current cost and selects minimum cost of previous way or the other way with cost M 
"""
def optimal_plan(ny, sf, M, n):
	first = ny[0]
	second = sf[0]
	old_first = first
	old_second = second

	for i in range (1, n):
		first = ny[i] + min(old_first, old_second+M)
		second = sf[i] + min(old_second, old_first+M)
		old_first = first
		old_second = second
	return min(first, second)

"""**************************************** ANSWER - 2 ****************************************"""
"""
-this function sorts by finish times and start times respect to finish times
"""
def sort_finishtime(start_time, finish_time):

	for i in range(0,len(finish_time)):
		for j in range (i+1, len(finish_time)):
			if(finish_time[i] > finish_time[j]):
				temp = finish_time[i]
				finish_time[i] = finish_time[j]
				finish_time[j] = temp
				temp = start_time[i]
				start_time[i] = start_time[j]
				start_time[j] = temp
			elif(finish_time[i] == finish_time[j]):
				if(start_time[i] > start_time[j]):
					temp = start_time[i]
					start_time[i] = start_time[j]
					start_time[j] = temp
	return
"""
-finds optimum start and finish times, and holds them start_jobsSelected and finish_jobsSelected
-this algorithm works respect to finish times, if the start time is late than previous time, we can join in session 
"""
def findOptimalScheule(start_time, finish_time, start_jobsSelected, finish_jobsSelected):
	sort_finishtime(start_time, finish_time)
	start_jobsSelected.append(start_time[0])
	finish_jobsSelected.append(finish_time[0])
	
	lastJob_start = start_time[0]
	lastJob_finish = finish_time[0]

	for i in range (1, len(start_time)):
		if(start_time[i] >= lastJob_finish):
			start_jobsSelected.append(start_time[i])
			finish_jobsSelected.append(finish_time[i])

			lastJob_start = start_time[i]
			lastJob_finish = finish_time[i]

	return

"""**************************************** ANSWER - 3 ****************************************"""
"""
-finds all the subarrays and holds them into array subs
"""
def findSubarrays(arr, index, sub, res):
	if(index == len(arr)):
		if(len(sub) != 0):
			res.insert(len(res), sub)
	else:
		findSubarrays(arr, index+1, sub, res)
		findSubarrays(arr, index+1, sub+[arr[index]], res)
	return
"""
-finds the subarray which total sum of elements equal zero
"""
def findSumofSub(arr):
	for i in range(0, len(arr)):
		if (sum(arr[i]) == 0):
			return arr[i]
	return None

"""**************************************** ANSWER - 4 ****************************************"""
"""
-takes two string to compare
-mismatch_penalty and gap_penalty values are positive, but multiplied by -1 to make negative number after calculate
-hold some values in matrix array and this values helped us to compare all the elements of strings
-if elements are equal, increase matched_count, if there is gap or mismatch, increase gap, mismatch respect to matrix
"""
def getMinimumPenalty(first_arr, second_arr):
	mismatch_penalty = 2
	gap_penalty = 1

	first_length = len(first_arr)
	second_length = len(second_arr)
	
	dp = ([[0 for i in range (second_length+first_length+1)] for i in range (second_length+first_length+1)]) 

	for i in range (0, second_length+first_length+1):
		dp[i][0] = i * gap_penalty
		dp[0][i] = i * gap_penalty
	
	for i in range (1, first_length+1):
		for j in range (1, second_length+1):
			if (first_arr[i-1] == second_arr[j-1]):
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(min(dp[i-1][j-1]+mismatch_penalty, dp[i-1][j]+gap_penalty), dp[i][j-1]+gap_penalty)

	total_size = first_length+second_length
	i = first_length
	j = second_length

	first_pos = total_size 
	second_pos = total_size 

	updated_first = ([0 for i in range (total_size+1)])
	updated_second = ([0 for i in range (total_size+1)])

	matched_count = 0

	while (i != 0 and j != 0):

		if (first_arr[i-1] == second_arr[j-1]):
			matched_count+=1

			updated_first[first_pos] = ord(first_arr[i - 1])
			first_pos -= 1
			updated_second[second_pos] = ord(second_arr[j - 1])
			second_pos -= 1
			i -= 1
			j -= 1

		elif (dp[i - 1][j - 1] + mismatch_penalty == dp[i][j]):
		
			updated_first[first_pos] = ord(first_arr[i - 1])
			first_pos -= 1
			updated_second[second_pos] = ord(second_arr[j - 1])
			second_pos -= 1
			i -= 1
			j -= 1

		elif (dp[i - 1][j] + gap_penalty == dp[i][j]):
		 
			updated_first[first_pos] = ord(first_arr[i - 1])
			first_pos -= 1
			updated_second[second_pos] = ord('_')
			second_pos -= 1
			i -= 1

		elif (dp[i][j - 1] + gap_penalty == dp[i][j]):

			updated_first[first_pos] = ord('_')
			first_pos -= 1
			updated_second[second_pos] = ord(second_arr[j - 1])
			second_pos -= 1
			j -= 1

	while (first_pos > 0):
	 
		if (i > 0):
			i -= 1
			updated_first[first_pos] = ord(first_arr[i])
			first_pos -= 1
		else:
			updated_first[first_pos] = ord('_')
			first_pos -= 1

	while (second_pos > 0):
	 
		if (j > 0):
			j -= 1
			updated_second[second_pos] = ord(second_arr[j])
			second_pos -= 1
		else:
			updated_second[second_pos] = ord('_')
			second_pos -= 1

	ind = 1
	for i in range(total_size,0,-1):
		if (chr(updated_second[i]) == '_' and chr(updated_first[i]) == '_'):

			ind = i+1
			break
	
	print("Alignment of sequence A and B:")

	for i in range(ind,total_size+1): 
		print(chr(updated_first[i]), end="") 
	print() 
	for i in range(ind,total_size+1): 
		print(chr(updated_second[i]), end="") 
	print()

	penalty_count = dp[first_length][second_length]
	penalty = penalty_count*-1
	total = (matched_count*2)+penalty

	return total

"""**************************************** ANSWER - 5 ****************************************"""
"""
-sorts array to calculate sum, because starting with smaller numbers, operation count will be smaller
-among the size of array, sum the first 2 element, delete these 2 element and add the result in the array until length of array is 1 
"""
def sumofarray(arr, cost):
	arr.sort()
	if(len(arr) == 1):
		return
	Sum = arr[0]+arr[1]
	cost.append(Sum)
	arr.append(Sum)
	arr.pop(0)
	arr.pop(0)
	sumofarray(arr,cost)

def main():
	"""**************************************** ANSWER - 1 ****************************************"""
	print ("******************************** ANSWER 1 ********************************")
	print ("***")
	NY = [2,7,3,5,10]
	SF = [9,5,7,3,2]
	M = 10
	print("Cost of an optimal plan: ", optimal_plan(NY, SF, M, len(NY)))
	print ("***")
	NY = [1,3,20,30]
	SF = [50,20,2,4]
	M = 10
	print("Cost of an optimal plan: ", optimal_plan(NY, SF, M, len(NY)))
	
	"""**************************************** ANSWER - 2 ****************************************"""
	print ("******************************** ANSWER 2 ********************************")
	print ("***")
	start_jobsSelected = []
	finish_jobsSelected = []
	start_time = [17,16,9,10,16,14,12,16]
	finish_time = [20,18,11,11,17,15,17,19]
	findOptimalScheule(start_time, finish_time, start_jobsSelected, finish_jobsSelected)
	print("Optimal schedule:")
	print("Start times:", start_jobsSelected)
	print("Finish times:", finish_jobsSelected)
	print ("***")
	start_jobsSelected = []
	finish_jobsSelected = []
	start_time = [1,3,2,0,5,8,11]
	finish_time = [3,4,5,7,9,10,12]
	findOptimalScheule(start_time, finish_time, start_jobsSelected, finish_jobsSelected)
	print("Optimal schedule:")
	print("Start times:", start_jobsSelected)
	print("Finish times:", finish_jobsSelected)
	print ("***")
	start_jobsSelected = []
	finish_jobsSelected = []
	start_time = [1,3,0,5,5,8]
	finish_time = [2,4,6,7,9,9]
	findOptimalScheule(start_time, finish_time, start_jobsSelected, finish_jobsSelected)
	print("Optimal schedule:")
	print("Start times:", start_jobsSelected)
	print("Finish times:", finish_jobsSelected)
	
	"""**************************************** ANSWER - 3 ****************************************"""
	print ("******************************** ANSWER 3 ********************************")
	print ("***")
	arr = [-2,4,-7,-5,22,11,1]
	subarrays = []
	temparr = []
	print("Array is: ")
	print(arr)
	findSubarrays(arr, 0, temparr, subarrays)
	result =[]
	result = findSumofSub(subarrays)
	print("The subset with the total sum of elements equal zero:")
	print(result)

	"""**************************************** ANSWER - 4 ****************************************"""
	print ("******************************** ANSWER 4 ********************************")
	print ("***")
	first = "ALIGNMENT"
	second = "SLIME"
	total = getMinimumPenalty(first, second)
	print("Cost is:", total)	
	print ("***")
	first = "ABDULLAH"
	second = "SADULLAH"
	total = getMinimumPenalty(first, second)
	print("Cost is:", total)
	print ("***")
	first = "ASGDHASGDHUCBSXS"
	second = "SJDGKAUCBSAK"
	total = getMinimumPenalty(first, second)
	print("Cost is:", total)
	
	"""**************************************** ANSWER - 5 ****************************************"""
	print ("******************************** ANSWER 5 ********************************")
	print ("***")
	arr = [4,1,2,5,3]
	cost = []
	sumofarray(arr, cost)
	print("Sum of array: ", sum(arr))
	print("Sum of optimal operation:",sum(cost))
	print ("***")
	arr = [21,6,17,93,3,41,34,73]
	cost = []
	sumofarray(arr, cost)
	print("Sum of array: ", sum(arr))
	print("Sum of optimal operation:",sum(cost))
	
main()