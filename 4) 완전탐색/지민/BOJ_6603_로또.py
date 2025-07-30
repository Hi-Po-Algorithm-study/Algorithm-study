def lotto(n,L):
    if len(L)==7:
        break
    
    

while True:
    S=list(map(int,input().split()))
    if S[0]==0:
        break
    visited=[0]*(len(S)-1)
    S.remove(S[0])
    L=[]
    for i in range(len(S)):
        if visited[i]==0:
            L.append(S[i])
            visited[i]=1
        # if len(L)==7:
        #     break
        print(L)

