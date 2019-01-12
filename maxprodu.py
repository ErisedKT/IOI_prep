import math 

T = int(input())
for _ in range(T):
    N, K = [int(x) for x in input().split()]
    if N <= K:
        print(-1)
        continue
    if N < (K+1)*(K+2)/2 - 1:
        print(0)
        continue
    X = list(range(2, K+1)) + [int(N - K*(K+1)/2 + 1)]
    f = math.factorial(K-1)
    prod = f*K * X[-1] * f * (X[-1] - 1)
    print(prod % (10**9 +7))
    
def max_prod(N, K):
    if N < (K+1)*(K+2)/2 - 1:
        return 0
    