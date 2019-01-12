from itertools import combinations
def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

T = int(input())
for i in range(T):
    N, M = [int(x) for x in input().split()]
    houses = []
    for j in range(N):
        bin = [int(x) for x in input()]
        for k in range(M):
            if bin[k] == 1:
                houses.append((j, k))
    dist = {}
    combs = list(combinations(houses, 2))
    for j in range(1, N + M - 1):
        dist[j] = 0
    for comb in combs:
        dist[manhattan_dist(comb[0], comb[1])] += 1
    for d in dist.values():
        print(d, end = " ")