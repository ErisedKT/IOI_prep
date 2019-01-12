T = int(input())
for i in range(T):
    N = int(input())
    rem = list(map(lambda x, y: int(y) - int(x), input().split(), input().split()))
    flag = False
    zero = N * [0]
    while (rem != zero):
        most = rem.index(max(rem))
        if most < 2:
            break
        for i in range(1, 4):
            rem[most + i - 3] -= i
        for r in range(N):
            if rem[r] < 0:
                flag = True
                break
        if flag:
            break
    if flag:
        print("NIE")
    else:
        print("TAK")