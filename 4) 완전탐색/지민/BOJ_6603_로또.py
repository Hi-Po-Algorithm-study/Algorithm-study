L=[]
while True:
    S=list(map(int,input().split()))
    if S[0]==0:
        break
    visited=[0]*(len(S)-1)
    # print(len(S))
    # print(S)
    S.remove(S[0])
    # print(S)
    # if len(L)==6:
    #     break
    for i in range(len(S)):
        if visited[i]==0:
            L.append(S[i])
            visited[i]=1
    if len(L)==6:
        break
    print(L)
    # print(visited)
#     if S[i][j]!= visited:
#         lst.append(S)