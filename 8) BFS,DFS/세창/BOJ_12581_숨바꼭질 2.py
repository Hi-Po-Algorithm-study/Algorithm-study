import sys
input=sys.stdin.readline

def bfs(start,end):
    queue=[start]
    visit=[0]*100001
    cnt=0

    visit[start]=1 #시작위치 방문

    while queue:
        x=queue.pop(0)

        if x==end:  #현재위치=도착위치
            cnt+=1  #cnt 1증가
        
        #이동 가능한 3가지
        for i in(x-1,x+1,2*x):
            if 0<i<=100000:

              

n,k=map(int,input().split())

a,b=bfs(n,k) 

print(a)
print(b)