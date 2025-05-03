import sys
input=sys.stdin.readline

def move(x,y):
    distance=y-x   #전체 거리

    # cnt=0   #공간이동 횟수
    # total=0 #총 이동 거리

    # while total<distance:  #총 이동 거리가 전체 거리보다 작으면
    #     cnt+=1             #공간이동 횟수 1증가

    
#############################################
t=int(input())

for _ in range(t):
    x,y=map(int,input().split())

    print(move(x,y))