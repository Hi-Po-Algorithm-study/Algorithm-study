import sys
N, P = map(int,sys.stdin.readline().split())
height = [0] * (N+1)
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
for i in range(N) :
    height[i+1] = a[i] - b[i]

roots = [[]for _ in range(N+1)]
for i in range(N-1) :
    s,e = map(int,sys.stdin.readline().split())
    roots[s].append(e)


def dfs(n,cnt, money) :
    if(not roots[n]) :
        return money
    for i in range (len(roots[n])) :
        c = cnt
        m = money
        end  = roots[n].pop()
        if(height[end] + c <0) :
            m-= (height[end]+c)
            c =0
        else :
            c += height[end]
        money = dfs(end,c,m)
        cnt = c
    return m


ans  = 0
if(height[P]>0) : 
    ans = dfs(P,height[P],0)
else :
    ans = dfs(P,0, -height[P])
print(ans)