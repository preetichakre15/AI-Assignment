import sys
A = [23,64,83,47,25,68]


for i in range(len(A)):
	
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
		
	A[i], A[min_idx] = A[min_idx], A[i]


print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" ")
