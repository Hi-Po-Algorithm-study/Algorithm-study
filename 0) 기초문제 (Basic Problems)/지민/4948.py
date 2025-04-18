import sys
input=sys.stdin.readline
def prime(n):
    lst=[False,False]+[True]*(2*n-1)
    prime=[]

    for i in range(2,2*n+1):
        if lst[i]:
            prime.append(i)
        for j in range(2*i,2*n+1,i):
            lst[j]=False
    # print(prime)

    # print(find(n))

    L=[]

    for x in prime:
        if x >n and x<=2*n:
            L.append(x) 
    # print(L)

    return(len(L))


while True:

    n=int(input())
    
    if n ==0:
        break
    print(prime(n))


#append 안하고 (리스안쓰고 cnt로 )