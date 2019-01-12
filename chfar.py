T = int(input())
for _ in range(T):
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A_sum = sum(A)
    A_square = [x**2 for x in A]
    sqr_sum = sum(A_square)
    i = 0
    while i < K and A_sum < sqr_sum:
        ind = A.index(max(A))
        temp = A[ind]
        A[ind] = 1
        A_square[ind] = 1
        A_sum = A_sum - temp + 1
        sqr_sum = sqr_sum - temp**2 + 1
        i += 1
    if A_sum == sqr_sum:
        print('YES')
    else:
        print('NO')