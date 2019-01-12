T = int(input())
for _ in range(T):
	N = int(input())
	A = [int(x) for x in input().split()]
	A_dict = {}
	for i in range(N):
		try:
			A_dict[A[i]].append(i)
		except KeyError:
			A_dict[A[i]] = [i]
	print(A_dict)
	for k in A_dict:
		if len(A_dict[k]) > 1:
			 
