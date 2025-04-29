# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# if N == 2:
#     print(M * M)
# else:
#     checkdp = [1 for _ in range(N)]
#     posibledp = [0 for _ in range(N)]
#     cantdp = [0 for _ in range(N)]

#     for i in range(3, N+1):
#         checkdp[i-1] = checkdp * M

N, M = map(int, input().split())
p = 998244353

dp = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]
# dp[n][m][p] = 길이 n이고 마지막 수가 m이고 마지막 수의 대소 관계가 p = <, =, > 일때 논산의 개수

for m in range(M):
    dp[0][m][1] = 1

for n in range(N - 1):
    for m in range(M):
        for i in range(m + 1, M):
            dp[n + 1][i][0] = (dp[n + 1][i][0] + sum(dp[n][m])) % p

        dp[n + 1][m][1] += sum(dp[n][m])

        for i in range(0, m):
            dp[n + 1][i][2] = (dp[n + 1][i][2] + dp[n][m][1] + dp[n][m][2]) % p

print(sum(map(sum, dp[N - 1])) % p)