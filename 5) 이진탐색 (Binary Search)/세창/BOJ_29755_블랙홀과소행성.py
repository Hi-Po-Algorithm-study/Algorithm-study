import sys
input=sys.stdin.readline

n,m=map(int,input().split())
blackhole=list(map(int,input().split()))


p=0

for _ in range(m):
    a,w=map(int,input().split())

    left=0
    right=n-1

    ans=0

    while left<=right:
        mid=(left+right)//2
        if blackhole[mid]>=a:
            ans=mid
            right=mid-1
        else:
            left=mid+1
            

print(p)