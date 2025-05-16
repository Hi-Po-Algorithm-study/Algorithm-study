import sys
input = sys.stdin.readline

N = int(input())
rec = int(input())
student = [float("inf") for i in range(101)] # 추천수 보관
recList = list(map(int, input().split())) # 추천수 입력값
candidate = [] # 정답

photo = [0 for _ in range(N)] # 후보 보관
photoN = [0 for _ in range(N)] # 오래된 놈

for num in recList:
    change = 0
    for i in range(N):
        if photo[i] == num: # 이미 후보자임
            student[num] += 1
            change = 1
            break
        elif photo[i] == 0: # 빈 액자
            photo[i] = num
            student[num] = 1
            for j in range(i):
                photoN[j] += 1
            change = 1
            break
    if change == 1: # 사진 바꿨음
        continue

    else: # 빈곳 없고 갈아끼기
        low = min(student)
        eliminate = []
        maxphotoN = 0
        for i in range(N):
            stuNum = photo[i]
            if student[stuNum] == low:
                maxphotoN = max(maxphotoN, photoN[i])
                eliminate.append((stuNum, photoN[i]))
     
        for die in eliminate:
            dieNum, dieN = die
            if dieN == maxphotoN:
                student[dieNum] = float('inf')
                student[num] = 1
                for u in range(N):
                    if photo[u] == dieNum:
                        photo[u] = num
                        for k in range(N):
                            photoN[k] += 1
                        photoN[u] = 0
                        break 

photo.sort()
for i in range(N):
    if photo[i] == 0:
        continue
    else:
        candidate.append(photo[i])
print(*candidate)
            
