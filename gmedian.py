#from itertools import combinations
T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    sublists = (2 ** (N-1)) % (10**9 + 7)
#    for i in range(2, N+1, 2):
#        combs = list(combinations(A, i))
#        for c in combs:
#            if c[i//2 -1] == c[i//2]:
#                sublists += 1
    print(int(sublists) % (10**9 + 7))
    

