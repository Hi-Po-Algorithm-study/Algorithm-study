import sys
from collections import deque
input = sys.stdin.readline

while(True):
    n = int(input())
    if (n == 0):
        break

    # 범위에 2가 있으면 걸러져서 예외처리
    if (n == 1):
        print(1)
        continue

    if (n == 2):
        print(1)
        continue

    maxDivide = int((2*n)**0.5) +1 # 최대값의 제곱근 까지만 검사하면 됨
    
    check = deque([])
    
    for num in range(n+1, (2*n)+1): # 체크해야 하는 범위 수
        for divide in range(2, maxDivide+1): # 나눌 수 (2 ~ 제곱근(최대값))
            if num % divide == 0: # 나누어 떨어지면 break
                break
            if divide == maxDivide and num % divide != 0: # 끝까지 나누었는데 안나눠 떨어지면 큐에 넣기
                check.append(num)
    
    print(len(check))



    # for num in range(n+1, (2*n)+1):
    #     if num % 2 != 0:
    #         check.append(num)
    # # 2의 배수인거 거르고 넣기

    # for divide in range(3, maxDivide+1):
    #     length = len(check)
    #     for i in range(length):
    #         number = check.popleft()
    #         if number % divide != 0:
    #             check.append(number)

    # print(len(check))


        

