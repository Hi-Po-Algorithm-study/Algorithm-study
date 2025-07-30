import sys

N = int(sys.stdin.readline())

def Hanoi(n, x, y) :
    if n>1 :
        Hanoi(n-1, x, 6-x-y)
    print(x,y)
    if n>1 :
        Hanoi(n-1, 6-x-y, y)


print(2**N-1)
Hanoi(N,1,3)




