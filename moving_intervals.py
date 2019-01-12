with open('cake_in.txt', 'r') as f_in:
    NUM_CASES = int(f_in.readline())
  #  for i in range(NUM_CASES):
    f = f_in.readline
    C, N, K = f().split(' ')
    C = int(C)
    N = int(N)
    K = int(K)
    cake_dict = {}
    for i in range(C):
        cake_dict[i + 1] = []
    for i in range(N):
        cakes = f().split(' ')
        start = int(cakes[0])
        end = int(cakes[1])
        for j in range(start, end + 1):
            cake_dict[j].append(i)
    if K == 0:
        fight = False
        for cake in cake_dict:
            if len(cake_dict[cake]) > 1:
                print('Bad')
                fight = True
                break
        if not fight:
            print('Good')
    else:
            
    
        
    