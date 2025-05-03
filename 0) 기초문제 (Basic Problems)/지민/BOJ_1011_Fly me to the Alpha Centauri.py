T=int(input())
for _ in range(T):
    x,y=map(int,input().split())
    s=y-x+1
    
visited=[False]*s
min_d=[]
cnt=0
def dfs(v):
    v=1
    visited[v]=True
    distance=y-x-1

    node=[[v]]
    for i in range(1,distance):
        k=i
        if i==distance:
            node[i].append(1)
        else:
            if k-1>=0:
                node[i].append(k)
                node[i].append(k-1)
                node[i].append(k+1)

    for ii in range(s):
        
        if visited[ii]==False and node[v][ii]:
            visited[ii]==True
            cnt+=1
    min_d.append(cnt)
    dfs(ii)
    
print(min(min_d))
