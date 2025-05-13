import sys
input=sys.stdin.readline

n=int(input())
q=[list(map(int,input().split())) for _ in range(n)]

ans=0

# 123~987 사이의 모든 수
for i in range(123, 988):
    # 영수의 세 자리

    # 중복 및 0이 들어가는 수 처리
    if 0 in a: continue


    strike=ball=0

    for i in range(3):
        if a[i]==b[i]:
            strike+=1
        elif a[i] in b:
            ball+=1


print(ans)


