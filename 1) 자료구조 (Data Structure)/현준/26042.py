import sys
from collections import deque
input = sys.stdin.readline

food = deque([])
maxStudent = 0


n = int(input())

lastStudent = n

for i in range(n):
    get = input().split()
    if get[0] == '1':
        food.append(int(get[1]))
        
        if maxStudent == len(food):

            lastStudent = min(lastStudent, food[-1])
        elif maxStudent <len(food):
                maxStudent = len(food)
                lastStudent = food[-1]

            
    else:
        food.popleft()

    # print(food)
    # print(maxStudent, lastStudent)
    # print()

print(maxStudent, lastStudent)