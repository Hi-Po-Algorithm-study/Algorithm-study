import sys
input = sys.stdin.readline

n = int(input())

boxSize = list(map(int, input().split()))

dp = [1 for _ in range(n)]


for i in range(n):
    for j in range(0,i):
        if boxSize[j] < boxSize[i]:
            dp[i] = max(dp[i], dp[j]+ 1)

print(max(dp))