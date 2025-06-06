import sys
input = sys.stdin.readline

N = int(input())

def star(i, n):
    
    if i == 0:
        return

    if i == 2**n:
        for _ in range(i):
            print('*', end="")
        star(i-1, n)
        return

    elif i == (2**n -1):
        for k in range(i):
            if k %2 == 1:
                print('*',end="")
            else:
                print(' ',end="")
        star(i-1, n)
        return

    elif i == (2**n - 2):
        for k in range(i):
            if k % 4 == 1:
                print('*',end="")
            elif k%4 ==2:
                print('*',end="")
            elif k%4 == 3:
                print(' ',end="")
            else:
                print(' ',end="")
        star(i-1, n)
        return

    else:
        for k in range(i):
            if k % 4 == 1:
                print('*',end="")
            elif k%4 ==2:
                print(' ',end="")
            elif k%4 == 3:
                print(' ',end="")
            else:
                print(' ',end="")
     
        star(i-1, n-1)
        return
    
star(2**N, N)

# num = 2**N

# while num != 0:

    