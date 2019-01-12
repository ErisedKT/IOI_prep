from itertools import combinations
from functools import reduce

def sect(x, y):
    return [max(x[0], y[0]), min(x[-1], y[-1])]
   
T = int(input())
for _ in range(T):
    N, K = [int(x) for x in (input().split())]
    segments = []
    for i in range(N):
        segments.append([int(x) for x in input().split()])
    comb = list(combinations(segments, K))
    all_intr = reduce(sect, segments)
    max_len = 0
    for c in comb:
        intr = reduce(sect, c)
        intrlen = intr[1] - intr[0]
        if intrlen > max_len:
            max_len = intrlen
    print(max_len)