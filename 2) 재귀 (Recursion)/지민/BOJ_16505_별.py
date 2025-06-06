N=int(input())
# L=[[]*(N+1)]
L=[]
for _ in range(N+1):
    L.append(0)

L[0]="*"
# L[1]="**\n*"

# print(L[1])

# for i in range(2,N):
#     L[N]=f"{L[N-1]}+{L[N-1]}\n{L[N-1]}"
# print(L[N])

# L[2]=f"{L[1]}{L[1]}\n{L[1]}"
# print(L[2])

L[1]=[["**"],["*"]]
L[2]=L[1][0]+L[1][0],L[1][1]+L[1][1]
print(*L[2][0])
print(*L[2][1])
print(*L[1][0])
print(*L[1][1])
