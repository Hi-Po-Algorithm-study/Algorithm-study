import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

focus = list(map(int, input().split()))
focus.sort()
gap = []
ans = 0

if N == 1: # 예외처리
    print(0)

else:
    for i in range(N-1):
        a = focus[i+1] - focus[i]
        gap.append(a)

    for i in range(K-1):
        maxGap = max(gap)
        for j in range(N):     
            if gap[j] == maxGap:            
                gap[j] = 0
                break
        
    for i in range(N-1):
        ans += gap[i]

    print(ans)