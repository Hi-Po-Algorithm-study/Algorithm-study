##dfs

N=int(input())
matrix=[list(map(int,input().split()))for _ in range(N)]
L=([]*N for _ in range(N))

s=(0,0)

visited=[[0] *N for _ in range(N)]

def dfs(x,y):
    visited[x][y]=True
    
    dx=[matrix[x][y],0]
    dy=[0,matrix[x][y]]
    
    for i in range(2):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
            dfs(nx,ny)
dfs(0,0)
if visited[N-1][N-1]==True:
    print("HaruHaru")
else:
    print("Hing")

# # print(matrix)
# dx=[1,0]
# dy=[0,1]
# for x in range(2):
#     nx=dx[x]
#     ny=dy[x]
    
# for i in range(N):
#     for j in range(N):
#         L.append()
        
#         if i + matrix[i][j]+nx>N:
#             print("Hing")
#         elif j+matrix[i][j]+ny>N:
#             print("Hing")
#         else:
#             break
# print(1)