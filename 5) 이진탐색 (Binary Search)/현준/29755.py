import sys
input = sys.stdin.readline

N, M = map(int, input().split())

blackhole = list(map(int, input().split()))
small = []

for _ in range(M):
    a, w = map(int, input().split())
    small.append((a,w))

blackhole.sort()
small.sort()

left = 0
right = 2000000000


while left < right:
    last = 0
    if right - left == 1:
        mid = right
        break

    mid = (left + right) // 2

    for i in range(M): # 소행성
        flag = 0
        pos, weight = small[i]
        for j in range(last, N): # 블랙홀
            if (pos - (mid / weight)) <= blackhole[j]and blackhole[j] <= (pos + (mid / weight)):
                last = j
                flag = 1
                break

        if flag == 0:
            # 문제있는거임 P가 작아
            left = mid
            break
    
    if flag == 1:
        right = mid

print(mid)
        

