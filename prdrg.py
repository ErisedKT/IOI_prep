data = [int(x) for x in input().split()]
num = [1, 1]
for j in range(2, 25):
	num.append(num[-1] + 2*num[-2])
for j in range(1, data[0]+1):
	print(num[data[j]-1], 2**data[j], end=" ")
