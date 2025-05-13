import sys
L, N, T = map(int, sys.stdin.readline().split())
dx = [-1, 1]
ball = [0] * N
LR = [0] * N
for i in range(N) :
    b, w = sys.stdin.readline().split()
    ball[i] = int(b)
    if w == 'R' :
        LR[i] = 1

cnt = 0
for _ in range(T) :
    point = set()
    for i in range(N) :
        x = ball[i] + dx[LR[i]]
        if 0<x<L+1 :
            ball[i] = x
            if x == 1 or x==L :
                if LR[i] == 0 :
                    LR[i] = 1
                else :
                    LR[i] = 0
            if x in point :
                cnt += 1
                for b in ball :
                    if b==x :
                        if LR[i] == 0 :
                            LR[i] = 1
                        else :
                            LR[i] = 0
            else :
                point.add(x)
        else :
            if LR[i] == 0 :
                LR[i] = 1
            else :
                LR[i] = 0
            point.add(ball[i])

print(cnt)

        