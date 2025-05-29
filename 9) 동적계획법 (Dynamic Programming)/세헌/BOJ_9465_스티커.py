import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(input())
    S = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    if N == 0:
        print(0)
        continue
    elif N == 1:
        print(max(S[0][0], S[1][0]))
        continue

    dp = [[0] * N for _ in range(2)]

    dp[0][0] = S[0][0]
    dp[1][0] = S[1][0]

    dp[0][1] = S[0][1] + dp[1][0]
    dp[1][1] = S[1][1] + dp[0][0]

    for i in range(2, N):
        dp[0][i] = S[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = S[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][N-1], dp[1][N-1]))
