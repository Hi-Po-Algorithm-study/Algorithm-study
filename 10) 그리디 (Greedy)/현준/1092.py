import sys
input = sys.stdin.readline

N = int(input())
crane = list(map(int, input().split()))
M = int(input())
boxWeight = list(map(int, input().split()))
moving = [0 for _ in range(M)]
craneCanMove = [0 for _ in range(N)]
crane.sort(reverse=True)
boxWeight.sort(reverse=True)
idx = 0
day = 0

print(crane)
print(boxWeight)
if boxWeight[0] > crane[0]:
    print(-1)
else:
    while True:
        day += 1
        for i in range(N):
            for j in range(len(boxWeight)):
                if boxWeight[i] <= crane[j]:
                    boxWeight.remove(boxWeight[i])
                    i -= 1
                    break


# while True:
#     for j in range(N-1, -1, -1):

#         for i in range(M-1, -1, -1):
#             if moving
