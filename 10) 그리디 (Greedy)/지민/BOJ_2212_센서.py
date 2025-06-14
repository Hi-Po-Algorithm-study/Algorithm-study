N=int(input())
K=int(input())

lst=list(map(int,input().split()))
lst.sort()

# print(lst)

max

while K==0:
    max=lst[1] - lst[0]
    K=K-1
    for i in range(2,N-1):
        n=lst[i]
        if n-lst[i-1]<max:
            n=lst[i+1]
        elif n-lst[i-1]>max:
            max=n-lst[i-1]
            K=K-1

        print(max)