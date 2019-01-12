T = int(input())
for _ in range(T):
    N, M, K, L = [int(x) for x in input().split()]
    A = sorted([int(x) for x in input().split()])
    inLine = [M]
    time = 0
    min_time = (M+1) * L
    for i in range(1, K+1):
        inLine.append(inLine[-1])
        if i % L == 0:
            inLine[i] -= 1
        if N != 0 and i == A[0]:
            inLine[-1] += 1
            time = inLine[i]*L - (i%L)
            del A[0]
            N -= 1
        else:
            time = (inLine[i]+1)*L - (i%L)
        if time < min_time:
            min_time = time
    print(min_time)