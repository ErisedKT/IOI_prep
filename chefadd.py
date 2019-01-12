from itertools import permutations

def unique_perms(s):
    return {"".join(p) for p in permutations(s)}

def num_perms(A, B, C):
    permsA = [int(x, 2) for x in unique_perms(A)]
    permsB = [int(x, 2) for x in unique_perms(B)]
    permsA.sort(reverse = True)
    permsB.sort()
    count = 0
    m1 = C - permsA[0]
    j = 0
    while (permsB[j] < m1):
        del permsB[j]
    m2 = C - permsB[-1]
    while (permsA[-1] < m2):
        del permsA[-1]
    for perm in permsA:
        if C - perm in permsB:
            count += 1
    return count

T = int(input())
for i in range(T):
    intA, intB, intC = [int(x) for x in input().split()]      
    A = '00' + bin(intA)[2:]
    B = '00' + bin(intB)[2:]
    print(num_perms(A, B, intC))
    
    