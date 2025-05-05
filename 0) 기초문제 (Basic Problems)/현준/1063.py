import sys
from collections import deque
input = sys.stdin.readline

king, stone, N = map(str, input().split())
king_x, king_y = map(str, king)
stone_x, stone_y = map(str, stone)

def trans(str):
    if str == 'A':
        return 1
    if str == 'B':
        return 2
    if str == 'C':
        return 3
    if str == 'D':
        return 4
    if str == 'E':
        return 5
    if str == 'F':
        return 6
    if str == 'G':
        return 7
    if str == 'H':
        return 8
    
def retrans(a):
    if a == 1:
        return "A"
    if a == 2:
        return "B"
    if a == 3:
        return "C"
    if a == 4:
        return "D"
    if a == 5:
        return "E"
    if a == 6:
        return "F"
    if a == 7:
        return "G"
    if a == 8:
        return "H"
    
    

def kingMove(a):
    if a == 'B':
        return (0, -1)
    if a == 'L':
        return (-1, 0)
    if a == 'T':
        return (0, 1)
    if a == 'R':
        return (1, 0)
    if a == 'LB':
        return (-1, -1)
    if a == 'RB':
        return (1, -1)
    if a == 'LT':
        return (-1, 1)
    if a == 'RT':
        return (1, 1)
    
    


king_x = trans(king_x)
king_y = int(king_y)
stone_x = trans(stone_x)
stone_y = int(stone_y)
kingPos = (king_x, king_y)
stonePos = (stone_x, stone_y)

N = int(N)
moving = deque([])

for i in range(N):
    moving.append(input().strip())

while moving:
    next = moving.popleft()
    next_x, next_y = kingMove(next)

    if 0<king_x + next_x<9 and 0<king_y+next_y<9:
        if stone_x == king_x+next_x and stone_y == king_y+next_y:
            if 0<stone_x + next_x<9 and 0<stone_y+next_y<9: 
                stone_x += next_x
                stone_y += next_y
            else:
                continue
        king_x += next_x
        king_y += next_y
    else: 
        continue       
    
king_x_ans = retrans(king_x)
stone_x_ans = retrans(stone_x)

print(king_x_ans, king_y, sep="")
print(stone_x_ans, stone_y, sep="")

