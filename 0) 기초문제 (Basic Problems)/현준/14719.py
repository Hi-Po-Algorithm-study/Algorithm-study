import sys
input = sys.stdin.readline

H, W = map(int, input().split())

getWorld = list(map(int, input().split()))
total = 0

# 이차원 배열이 필요함

world = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if getWorld[j] > i:
            world[i][j] = 1

for i in range(H): 
    rain = 0
    can = 0
    front = False
    back = False

    for j in range(W): 

        if world[i][j] == 1:
            if front == False:
                front = True
            else:
                rain += can
                can = 0
        else:
            # 0일때
            if front == True:
                can += 1
    # print("dd", rain)
    total += rain

print(total)