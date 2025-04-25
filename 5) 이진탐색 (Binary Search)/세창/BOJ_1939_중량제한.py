import sys
from collections import deque
input=sys.stdin.readline

def bfs(land_1,land_2,mid):
    visit=[False]*(n+1)

    q=deque()

    while q:
        current=q.popleft

        if current==land_2: return True #도착점 도달하면 True반환


####################################################

n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))  #a에서 b / c는 중량제한
    graph[b].append((a,c))  #b에서 a / c는 중량제한

land_1,land_2=map(int,input().split())

####################################################

max_weight=1_000_000_000

min=1           #중량 최소값
max=max_weight  #중량 최대값

while min<max:
    mid=(min+max)//2 #중간값

    min=mid+1
    max=mid-1