from math import gcd

T = int(input())
for t in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    changes = 0
    if N == 1:
        print(changes)
        print(A[0])
        continue
    elif N == 2:
        if gcd(A[0], A[1]) != 1:
            changes += 1
            for j in range(2, 50):
                if gcd(A[0], j) == 1:
                    A[1] = j
                    break
        print(changes)
        print(A[0], A[1])
        continue
    valid = N * ['F'] 
    for i in range(N - 1):
        if valid == N * ['T']:
            break
        for j in range(i + 1, N):
            if valid[i] == 'T' and valid[j] == 'T':
                continue
            else:
                if gcd(A[i], A[j]) == 1:
                    valid[i] = 'T'
                    valid[j] = 'T'
    for i in range(N-1):
        if valid[i] == 'F':
            changes += 1
            for j in range(2, 50):
                if gcd(A[i], A[i+1]) == 1:
                    A[i] = j
    if valid[N-1] == 'F':
        changes += 1
        for j in range(2, 50):
            if gcd(A[N-1], A[N-2]) == 1:
                A[N-1] = j     
    print(changes)
    for i in A:
        print(i, end = " ")
            