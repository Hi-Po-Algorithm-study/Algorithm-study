import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

C =set()
cnt = 0

for i in range(N) :
    if T[i] in C:
        C.remove(T[i])
        cnt += 1
    else :
       C.add(M-T[i])

print(cnt) 