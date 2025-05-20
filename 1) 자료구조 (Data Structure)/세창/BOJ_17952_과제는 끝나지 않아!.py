import sys
input=sys.stdin.readline

n=int(input())

homework=[]
scores=0

for _ in range(n):
    info=list(map(int,input().split()))

    if info[0]==1:
        homework.append([info[1],info[2]]) #  info[1]:점수, info[2]:시간
    
    if homework: 
        homework[-1][1]-=1          # 가장 최근에 받은 과제 남은 시간 1분 차감
        if homework[-1][1]==0:      # 과제 남은 시간이 0분이면,
            scores+=homework[-1][0] # 해당 과제의 점수를 scores에 더한다

            homework.pop()

print(scores)