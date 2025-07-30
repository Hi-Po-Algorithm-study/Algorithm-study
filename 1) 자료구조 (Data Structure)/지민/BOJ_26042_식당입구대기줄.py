from collections import deque
N=int(input())

L=deque()
mx=0
mn=1000000000
for _ in range(N):
    a=input()
    if a[0]=='1':
        L.append(int(a[-1]))
        mx=max(mx,len(L))
        if len(L)==mx:
            mn=min(mn,L[-1])
            
    else:
        L.popleft()
        
print(mx,mn)
        
        
    # a,b=map(int,input().split())
    # if a==1:
    #     L.append(b)
    #     mx=max(mx,len(L))
    # else: 
    #     L.popleft()
        
    # print(mx)