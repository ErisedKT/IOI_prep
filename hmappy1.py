def find_long(s, K, N):
    count = 0
    cur_count = 0
    for i in range(N):
        if cur_count == K:
            return K
        if (i < N and s[i] == 1):
            cur_count += 1
        else:
            if cur_count > count:
                count = cur_count
            cur_count = 0
    if cur_count > count:
        return cur_count
    return count

N, Q, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
S = str(input())
i = 0
#for s in S:
#    if s == '!':      
#        A = [A[-1]] + A[:-1]
#    else:
#	   print(find_long(A, K, N))
while i < Q:
    shifts = 0
    while i < Q and S[i] == '!':
        shifts += 1
        i += 1
    if shifts != 0:
        A = [A[-shifts]] + A[:-shifts]
    tells = 0
    while i < Q and S[i] == '?':
        tells += 1
        i += 1
    if tells != 0:
        tell = find_long(A, K, N)
    for j in range(tells):
        print(tell)
        
