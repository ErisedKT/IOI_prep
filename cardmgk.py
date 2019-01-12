T = int(input())
for i in range(T):
    N = int(input())
    deck = [int(x) for x in input().split()]
    flag = False
    for j in range(1, N):
        if deck[j] < deck[j-1]:
            break
    j += 1
    while (j < N):
        if deck[j] < deck[j-1] or deck[j] > deck[0]:
            print("NO")
            flag = True
            break
        j += 1
    if not flag:
        print("YES")