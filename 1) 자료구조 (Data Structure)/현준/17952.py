import sys
input = sys.stdin.readline

N = int(input())
work = []
score = 0

for _ in range(N):

    get = input().strip()

    if get == '0': # 하던 과제하기
        if work: # 하고있는 과제가 없을 수도
            getScore, time = work.pop() # 하던 과제

            if (time-1) > 0: # 하던 과제 남음
                work.append((getScore,time-1))
                
            else: # 하던 과제 끝
                score += getScore


    else: # 과제 받은거 하기
        one, A, T = map(int, get.split())

        if (T-1) > 0: # 받은 과제 남음
            work.append((A, T-1))

        else: # 받은 과제 끝
            score += A


print(score)