import sys
input = sys.stdin.readline

N = int(input())
stone = [1, 3]
dp = [-1 for _ in range(N+1)]
# 0은 상근이 승 1은 창영이 승
# dp[n] 은 n개 일때 이기는 사람
dp[1] = 1

i = 1
k = 0

def stoneGame(i, who):

    if dp[i] == -1:
        dp[i] = who
    
    if i+1 <= N:
        if dp[i+1] == -1:
            stoneGame(i+1, who+1)
    if i+3 <= N:
        if dp[i+3] == -1:
            stoneGame(i+3, who)

    
stoneGame(1, 1)

if dp[N] % 2 == 1:
    print('CY')
else:
    print("SK")