from itertools import combinations
N = int(input())
strengths = [int(x) for x in input().split()]
revs = sum([abs(t[0] - t[1]) for t in list(combinations(strengths, 2))])
print(revs)