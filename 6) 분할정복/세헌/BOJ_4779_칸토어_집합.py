import sys

N = sys.stdin.readlines()

for i in N :
    n = int(i)
    T = ['-' for _ in range(3**n)]
    cnt = len(T)
    
    while (cnt>1) :
        cnt = cnt//3
        delete = cnt
        for d in range(delete,delete*2) :
            T[d] = ' '
    print(''.join(T))
