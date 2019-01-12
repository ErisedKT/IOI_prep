T = int(input())
for i in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    j = 1
    last = -2
    if A.count(-1) == N:
        print("inf")
        continue
    while j < N:
        if A[j] != -1 and A[j-1] != -1:
            
        