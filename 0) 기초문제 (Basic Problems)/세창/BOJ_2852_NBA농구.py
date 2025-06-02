import sys
input=sys.stdin.readline

n=int(input())

team1=0
team2=0
cur_lead=0   # >0:팀1 리드, <0:팀2 리드, 0:동점
score_time=0 # 득점 시간
end_time=2880

for _ in range(n):
    team,time=input().split()
    minute,second=map(int, time.split(":"))
    now=(minute*60)+second # 현재 득점 시간이 몇 초인지

    if team=='1':
        cur_lead+=1
    else:
        cur_lead-=1

    if cur_lead>0:
        team1+=now-score_time
    elif cur_lead<0:
        team2+=now-score_time
        