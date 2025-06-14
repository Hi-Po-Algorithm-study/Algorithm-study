import sys
N, M = map(int, sys.stdin.readline().split())
black = list(map(int, sys.stdin.readline().split()))
planet_a = []
planet_w = []
for _ in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    planet_a.append(x)
    planet_w.append(y)

def hole(m,w,P) :
    if m <= P/w :
        return True
    else :
        return False
left = 0
right = 200000000


while left < right :
    mid = (left + right) // 2
    for i in range(M) :
        mn = 2000000
        for j in range(last, N) :
            nn = mn 
            if black[j] < planet_a[i] :
                mn = min(mn, planet_a[i] - black[j])
            else :  
                mn = min(mn, black[j] - planet_a[i])
            if mn != nn :
                last = black[j]
        if not hole(mn, planet_w[i],mid):
            left = mid + 1 
    if left != mid :
        right = mid

print(left)