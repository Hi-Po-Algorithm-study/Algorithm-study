import sys
input=sys.stdin.readline

H,W=map(int,input().split())  # H는 세로(높이), W는 가로
block=list(map(int,input().split())) # 블록 높이

total_water=0

for i in range(1,W-1):  # 양 끝은 제외

    # 왼쪽 최대 높은 벽
    left_max=0
    for j in range(0,i):
        left_max=block[j]

    # 오른쪽 최대 높은 벽
    right_max=0
    for j in range(i+1,W):
        if block[j]>right_max:
            right_max=block[j]

    wall=min(left_max,right_max)

    water=wall-block[i]

    if water>0:
        total_water+=water

print(total_water)