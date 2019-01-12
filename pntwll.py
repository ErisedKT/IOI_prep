T = int(input())
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    wall = [C[0]]*H[0]
    for i in range(1, N):
        if H[i] <= len(wall):
            wall = [C[i]]*H[i] + wall[H[i]:len(wall)]
        else:
            wall = [C[i]]*H[i]
    wall = set(wall)
    print(len(wall))