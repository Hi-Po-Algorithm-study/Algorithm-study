n=int(input())
lst=list(map(int,input().split()))
s=int(input())

# print(lst)
visited=[False]*(n+1)
# cnt=0
def dfs(v):
    visited[v]=True
    cnt=0
    num=lst[v]

    while True:
        if v+num <=n and visited[v+num] == False:
            cnt+=1
            visited[v+num] =True
            
        elif v-num >=0 and visited[v-num] == False:
            cnt+=1
            visited[v-num] =True
            
        else:
            return False

        return(cnt)
        
ans=dfs(s)
print(ans)