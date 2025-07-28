from collections import deque
N=int(input())

L=deque()
M=[]
for i in range(1,N+1):
    L.append(i)

if N==1:
    print(1)
else:
    for j in range(N):
        b=L.popleft()
        if len(L)>0:
            a=L.popleft()
            L.append(a)
        
            M.append(b)
            
        if len(L)==1:
            M.append(L[0])
            
        
print(*M)
