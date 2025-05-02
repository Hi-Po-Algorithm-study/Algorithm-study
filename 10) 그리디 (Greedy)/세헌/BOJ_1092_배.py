import sys
import math
C = int(sys.stdin.readline())
Crane = list(map(int,sys.stdin.readline().split()))

B = int(sys.stdin.readline())
Box = list(map(int,sys.stdin.readline().split()))

Crane.sort()
Box.sort()
if Crane[-1] < Box[-1] :
    print(-1)
    exit()
time = [0] * C
index = 0
for i in range(C) :
    while(index<B) :
        if Crane[i] >= Box[index] :
            time[i] = time[i] + 1
            index += 1
        else :
            break

mx = max(time)
cnt = 0
for i in range(C-1,-1,-1) :
    if time[i] == mx :
        mx = math.ceil((cnt+mx) / (C-i))
        break
    else :
        cnt += time[i]
print(mx)