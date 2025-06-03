import sys
input = sys.stdin.readline

n = int(input())

boxSize = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

# 점화식
# dp[i] 가 i 번째 최대 상자의 개수

dp[0] = 1 # i 번째 최대
dp2[0] = 1 # i 번째 끼고 최대
maxi = 0
for i in range(n):
    
    if i == 0:
        maxi = boxSize[i]
        continue
    else:

        if boxSize[i] > maxi:
            dp[i] = dp[i-1] + 1
            dp2[i] = dp2[i-1] + 1
            maxi = boxSize[i]

        elif boxSize[i] == maxi:
            dp[i] = dp[i-1]
            dp2[i] = dp2[i-1]

        else:
            check = 0
            for j in range(i-1, 0, -1):
                if boxSize[j] < boxSize[i]:
                    check = j
                    break

            dp[i] = max(dp[i-1], dp2[check] + 1)
            #여기서도 바꿔줘야하는거 같은데
            
            dp2[i] = dp2[check] + 1


# print(dp)
# print(dp2)
print(max(dp[-1], dp2[-1]))