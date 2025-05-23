import sys
input=sys.stdin.readline

n=int(input()) # 갑옷 개수
m=int(input()) # 갑옷을 만드는데 필요한 수
arr=list(map(int,input().split()))

arr.sort() # 오름차순

cnt=0
start=0
end=n-1

while start<end:
    total=arr[start]+arr[end]
    if total==m:
        cnt+=1
        start+=1
        end-=1
    elif total<m:
        start+=1
    else:
        end-=1

print(cnt)