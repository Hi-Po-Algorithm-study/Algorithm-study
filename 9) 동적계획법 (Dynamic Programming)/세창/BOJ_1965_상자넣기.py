import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

dp=[1]*n 
# 1 ≤ n ≤ 1000

for i in range(1,n):
    for j in range(i):  # 앞쪽이랑 비교
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1) 
        else: 
            dp[i]=min(dp[i]-1,dp[j]) 

print(max(dp))

# arr=[1,6,2,5,7,3,5,6]

# dp=[1,1,1,1,1,1,1,1]

# dp=[1,2,2,3,4,4,5,6]
# dp=[1,2,2,3,4,3,4,5]