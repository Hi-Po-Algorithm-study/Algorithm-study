import sys
K, S, N = sys.stdin.readline().split()
N = int(N)
move = list(sys.stdin.readline().strip() for _ in range(N))
ky, kx = K.strip()
sy, sx = S.strip()
kx = int(kx)
sx = int(sx)

# 이동 방법 
Go = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# move값을 알맞는 dx, dy의 인덱스로 변경
for i in range(N) :
    for g in range(8) :
        if move[i] == Go[g] :
            move[i] = g
            break



y = ['A','B','C','D','E','F','G','H']
for i in range(8) :
    if ky == y[i] :
        ky = i+1
        break
for i in range(8) :
    if sy == y[i] :
        sy = i+1
        break

for i in range(N) :
    index = move[i]
    if 0 <kx + dx[index] < 9 and 0 <ky + dy[index] < 9 :
        kx = kx + dx[index]
        ky = ky + dy[index]
   
    if  kx == sx and  ky == sy :
        if 0 <sx + dx[index] < 9 and 0 <sy + dy[index] < 9 :
            sx = sx + dx[index]
            sy = sy + dy[index]
        else : 
            kx = kx - dx[index]
            ky = ky - dy[index]
ky = y[ky-1]
sy = y[sy-1]
k = ky+str(kx)
s = sy + str(sx)
print(k)
print(s)
