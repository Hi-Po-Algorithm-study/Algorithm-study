import sys
input = sys.stdin.readline

N = int(input())
numList = [[0,0,0] for _ in range(N)]
strikeList = [0 for _ in range(N)]
ballList = [0 for _ in range(N)]
check = [-1 for _ in range(1000)]


for i in range(1000):
    if i < 100:
        break
    else: #세자리 일때
        num1 = i // 100
        num2 = i // 10 - (i // 100 * 10)
        num3 = i - (i//10*10)
        if num1 != 0 and num2 != 0 and num3 != 0:
            if num1 != num2 and num2 != num3 and num1 !=num3:
                check[i] = 0

for i in range(N):
    number, strike, ball = map(int, input().split())
    numList[i][0] = number // 100
    numList[i][1] = number // 10 - (number // 100 * 10)
    numList[i][2] = number - (number//10*10)

    strikeList[i] = strike
    ballList[i] = ball

for i in range(N):
    if strike[i] == 3:
        print('1')
        break
    elif strike[i] == 2 and ball[i] == 0:
        for j in range(1, 10):
            if j != numList[i][0] and j != numList[i][1]:
                check[numList[i][0] * 100 + numList[i][1] * 10 + j] += 1
        for j in range(1, 10):
            if j != numList[i][1] and j != numList[i][2]:
                check[numList[i][1] * 10 + numList[i][2] + j * 100] += 1
        for j in range(1, 10):
            if j != numList[i][0] and j != numList[i][2]:
                check[numList[i][0] * 100 + numList[i][2] + j * 10] += 1
    elif strike[i] == 1 and ball[i] == 0:
        for j in range(1, 10):
            for k in range(1, 10):
                if j != numList[i][0] and k != numList[i][0] and j != k:
                    check[numList[i][0] * 100 + k * 10 + j] += 1
        for j in range(1, 10):
            for k in range(1, 10):
                if j != numList[i][1] and k != numList[i][1] and j != k:
                    check[numList[i][1] * 10 + k * 100 + j] += 1
        for j in range(1, 10):
            for k in range(1, 10):
                if j != numList[i][2] and k != numList[i][2] and j != k:
                    check[numList[i][2] + k * 100 + j * 10] += 1

    elif strike[i] == 1 and ball[i] == 1:
        for j in range(1, 10):
            if j != numList[i][0] and j != numList[i][1]:
                check[numList[i][0] * 100 + j * 10 + numList[i][1]] += 1
            if j != numList[i][0] and j != numList[i][2]:
                check[numList[i][0] * 100 + j + numList[i][2] * 10] += 1
        for j in range(1, 10):
            if j != numList[i][1] and j != numList[i][0]:
                check[numList[i][1] * 10 + j * 100 + numList[i][0]] += 1
            if j != numList[i][1] and j != numList[i][2]:
                check[numList[i][1] * 10 + j + numList[i][2] * 100] += 1
        for j in range(1, 10):
            if j != numList[i][2] and j != numList[i][0]:
                check[numList[i][2] + j * 100 + numList[i][0] * 10] += 1
            if j != numList[i][2] and j != numList[i][1]:
                check[numList[i][2] + j * 10+ numList[i][1] * 100] += 1
        

    elif strike[i] == 1 and ball[i] == 2:
        check[numList[i][0] * 100 + numList[i][2] * 10 + numList[i][1]] += 1
        check[numList[i][2] * 100 + numList[i][1] * 10 + numList[i][0]] += 1
        check[numList[i][1] * 100 + numList[i][0] * 10 + numList[i][2]] += 1

    elif strike[i] == 0 and ball[i] == 0:
        ##
    elif strike[i] == 0 and ball[i] == 1:
        ##
    elif strike[i] == 0 and ball[i] == 2:
        ##
    elif strike[i] == 0 and ball[i] == 3:
        check[numList[i][1] * 100 + numList[i][2] * 10 + numList[i][0]] += 1
        check[numList[i][2] * 100 + numList[i][0] * 10 + numList[i][1]] += 1