import sys
input=sys.stdin.readline

def sosu(i):

    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return False
    return True

######################################

while True:
    
    n=int(input())

    if n==0: break 

    cnt=0

    for i in range(n+1,2*n+1):
        if sosu(i):
            cnt+=1

    print(cnt)