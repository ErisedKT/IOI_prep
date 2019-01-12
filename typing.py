def hand(l):
    if l == 'd' or l == 'f':
        return 'l'
    return 'r'
T = int(input())
for i in range(T):
    time = 0
    N = int(input())
    words = {}
    for j in range(N):
        t = time
        w = input()
        if w in words:
            time += 0.5 * words[w]
        else:   
            time += 2
            for k in range(1, len(w)):
                if hand(w[k]) != hand(w[k-1]):
                    time += 2
                else:
                    time += 4
            words[w] = time - t
    print(int(time))