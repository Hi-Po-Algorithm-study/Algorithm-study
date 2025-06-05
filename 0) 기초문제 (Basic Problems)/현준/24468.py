import sys
input = sys.stdin.readline

L, N, T = map(int, input().split())
ans = 0
ball = [0 for _ in range(N)]
dir = []

for i in range(N):
    S, C = map(str, input().split())
    ball[i] = int(S)
    dir.append(C)

for _ in range(T):
    # 공 움직이기
    for i in range(N):
        if dir[i] == 'R':
            if ball[i] == L:
                ball[i] = L-1
                dir[i] = 'L'
            else:
                ball[i] += 1
                
        else:
            if ball[i] == 0:
                ball[i] = 1
                dir[i] = 'R'
            else:
                ball[i] -= 1

    # 충돌여부 체크
    for i in range(N-1):
        
        if ball[i] == ball[i+1]:
            ans += 1
            if dir[i] == 'R':
                dir[i] = 'L'
            else:
                dir[i] = 'R'

            if dir[i+1] == 'R':
                dir[i+1] = 'L'
            else:
                dir[i+1] = 'R'
    print(ball)
    print(dir)
    print()

print(ans)