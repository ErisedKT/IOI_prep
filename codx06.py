import math
T = int(input())
for _ in range(T):
	N = int(input())
	S, k = [int(x) for x in input().split()]
	sumA = sum([int(x) for x in input().split()])
	print(max(0, math.ceil((S - sumA)/k)))
