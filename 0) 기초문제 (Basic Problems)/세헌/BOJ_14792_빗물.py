import sys 
H, N = map(int, sys.stdin.readline().split())
top = list(map(int, sys.stdin.readline().split()))

mx = max(top)
mn = min(top)
front = top[0]
back = top[-1]



x = 0
rain = 0 
for i in range(N) :
    if top[i] == mx :
        x = i
        break
    if top[i] < front :
        rain += (front - top[i])
    elif top[i] > front :
        front = top[i]

y = 0
if x != N-1 :
    for i in range(N-1,x,-1) :
        if top[i] == mx :
            y = i
            break
        if top[i] < back :
            rain += (back - top[i])
        elif top[i] > back :
            back = top[i]

    if x != y :
        for i in range(x,y) :
            rain += (mx - top[i])
if N == 2 :
    rain = 0   
print(rain)