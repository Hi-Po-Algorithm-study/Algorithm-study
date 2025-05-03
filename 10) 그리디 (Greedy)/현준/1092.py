import sys
input = sys.stdin.readline

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
boxWeight = list(map(int, input().split()))
crane.sort(reverse=True)
boxWeight.sort(reverse=True)
idx = 0
day = 0

print(crane)
print(boxWeight)
if boxWeight[0] > crane[0]:
    print(-1)
else:
    boxIdx = 0
    craneIdx = 0
    moving = [0 for _ in range(M)]
    while True:
        craneCanMove = [0 for _ in range(N)]
        
        while True:
            if boxWeight[boxIdx] <= crane[craneIdx]:
                moving[boxIdx] = 1
                craneCanMove[craneIdx] = 1
            

# while True:
#     for j in range(N-1, -1, -1):

#         for
#  i in range(M-1, -1, -1):
#             if moving
