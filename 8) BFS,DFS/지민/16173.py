##

N=int(input())
matrix=[list(map(int,input().split()))for _ in range(N)]
L=([]*N for _ in range(N))
# print(matrix)
dx=[1,0]
dy=[0,1]
for x in range(2):
    nx=dx[x]
    ny=dy[x]
    
for i in range(N):
    for j in range(N):
        L.append()
        
        if i + matrix[i][j]+nx>N:
            print("Hing")
        elif j+matrix[i][j]+ny>N:
            print("Hing")
        else:
            break
print(1)