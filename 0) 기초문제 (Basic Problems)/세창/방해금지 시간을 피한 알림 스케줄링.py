import sys
input=sys.stdin.readline

def sol(noti_time, DND):
    hh,mm=map(int,noti_time.split(":"))
    cur=hh*60+mm # 분 단위

    for _ in range(2880): # 48시간
         

    return "impossible"

#########################################

noti_time=input().strip()
n=int(input().strip())
DND=[input().strip() for _ in range(n)]

res=sol(noti_time, DND)

print(res)
