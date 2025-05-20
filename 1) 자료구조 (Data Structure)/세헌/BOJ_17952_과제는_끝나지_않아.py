import sys
N = int(sys.stdin.readline())
stack = []
ans = 0
for i in range(N) :
    C = list(map(int, sys.stdin.readline().split()))
    
    if C[0]!=0 :
        stack.append([C[1],C[2]])
    if stack :
        a, t = stack.pop()
        t -= 1
        if t == 0 :
            ans += a
        else :
            stack.append([a,t])

print(ans)