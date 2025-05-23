import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

number = list(map(int, input().split()))
cnt = 0

number.sort()

for i in range(N):
    for j in range(i+1, N):
        if number[i] + number[j] == M:
            cnt += 1

print(cnt)