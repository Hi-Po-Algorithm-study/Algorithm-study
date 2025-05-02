import sys
N, M = map(int, sys.stdin.readline().split())
dp = [0] * (M+1)
cnt = 1
if(N==2) :
    cnt = M * M
elif N==1 :
    cnt = M
else :
    dp[1] = 0
    for i in range(2,M+1) :
        dp[i] = dp[i-1] + ((M-1)*(M-1)) 
    for i in range(N) :
        cnt =cnt * M
    if(N>3) :
        a = dp[M]
        for i in range(N-2) :
            dp[M] = dp[M]*M
        dp[M] - a
cnt = cnt - dp[M] 
print(cnt%998244353)


import sys
div = 998_244_353
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    before = [[0] * 3 for _ in range(M + 1)]
    now = [[0] * 3 for _ in range(M + 1)]
    for m in range(1, M + 1):
        before[m][1] = 1
    for n in range(1, N):
        sum_ = 0
        for m in range(M, 0, -1):
            sum_ = (sum_ + before[m][0] + before[m][1]) % div
            now[m-1][0] = sum_
        now[1][1] = (before[1][0] + before[1][1] + before[1][2]) % div
        sum_ = now[1][1] % div
        for m in range(2, M + 1):
            now[m][2] = sum_
            now[m][1] = (before[m][0] + before[m][1] + before[m][2]) % div
            sum_ = (sum_ + now[m][1]) % div
        before = [row[:] for row in now]
        now = [[0] * 3 for _ in range(M + 1)]
    answer = 0
    for m in range(1, M + 1):
        answer = (answer + before[m][0] + before[m][1] + before[m][2]) % div
    print(answer)
if __name__ == "__main__":
    main()

# import sys
# input = sys.stdin.readline

# MOD = 998244353

# N, M = map(int, input().split())

# def power(x, y, mod):
#     result = 1
#     x = x % mod
#     while y > 0:
#         if y % 2 == 1:
#             result = (result * x) % mod
#         y = y // 2
#         x = (x * x) % mod
#     return result

# # 전체 경우의 수
# total = power(M, N, MOD)

# # 특정 경우의 수 (문제에서 어떤 조건인지 정확히 명확하지 않아서, 
# # 만약 (M-1)^N 같은 경우라면 아래처럼)
# case = power(M-1, N, MOD)

# # 정답
# ans = (total - case + MOD) % MOD

# print(ans)

