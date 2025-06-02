import sys
N = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

for i in range(N) :
    for j in range(i) :
        if box[j] < box[i] :
            dp[i] = max(dp[j] + 1, dp[j])
    
print(max(dp))

