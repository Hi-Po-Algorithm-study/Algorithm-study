import sys
input=sys.stdin.readline

n=int(input()) #센서의 개수
k=int(input()) #집중국의 개수

sensor=list(map(int,input().split()))

#센서 오름차순 정렬
for i in range(n):
    for j in range(i+1,n):
        if sensor[i]>sensor[j]:
            sensor[i],sensor[j]=sensor[j],sensor[i]


#센서 간 거리
distance=[]
for i in range(1,n):
    distance.append(sensor[i]-sensor[i-1])


total=0

print(total)