T = int(input())
for i in range(T):
    day = 0
    num_told = 1
    N = int(input())
    svec = input().split()
    ivec = []
    for s in svec:
        ivec.append(int(s))
    to_tell = ivec[0]
    while num_told < N:
        temp = num_told
        num_told += to_tell
        for k in range(temp, num_told):
            if k >= N:
                break
            to_tell += ivec[k]
        day += 1
    print(day)