N,M=map(int,input().split())
lst=[]
weight=[]
graph=[[] for _ in range(M+1)]
for i in range(M):
    A,B,C=map(int,input().split())
    lst.append((A,B,C))
    weight.append(C)
    graph[A].append(B)
    graph[B].append(A)


sum1,sum2=map(int,input().split()) #1,3

# graph[sum1]\\\\\\\\\\;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;