import sys
N = int(sys.stdin.readline())
arr =list(sys.stdin.readline().strip()) 

A = 0
B = 1
dp = [[0, 0] for _ in range(N)]

if arr[0] == 'A':
    dp[0][A] = 0
    dp[0][B] = 1
else:
    dp[0][A] = 1
    dp[0][B] = 0

for i in range(1, N):
    isA = arr[i] == 'A'
    if isA:
        dp[i][A] = min(dp[i-1][A], dp[i-1][B] + 1)
        dp[i][B] = min(dp[i-1][A], dp[i-1][B]) + 1
    else:
        dp[i][B] = min(dp[i-1][B], dp[i-1][A] + 1)
        dp[i][A] = min(dp[i-1][B], dp[i-1][A]) + 1
print(min(dp[N-1][A], dp[N-1][B] + 1))