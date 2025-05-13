import sys
input=sys.stdin.readline

L,N,T=map(int,input().split())
# L=상자의 길이
# N=공의 개수
# T=시간

ball=[]

for _ in range(N):
    start,direction=input().split()
    start=int(start)
    ball.append((start,direction)) # 처음 공 위치/방향
    

cnt=0 # 충돌 횟수

for i in range(N):
    for j in range(i+1,N):
        start1,direction1=ball[i]
        start2,direction2=ball[j]


        if direction1=='R' and direction2=='L':
            distance=start2-start1

            if distance<=0:
                 continue

            # 두 공 사이 간격은 짝수 
            if (distance%2 != 0):
                continue


print(cnt)