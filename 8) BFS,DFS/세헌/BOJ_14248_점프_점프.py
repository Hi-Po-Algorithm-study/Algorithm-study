import sys

N = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline()) - 1

check = [0 for _ in range(N)] 
q = []
q.append(c)
check[c] = 1
cnt = 0

while(q) :
    cur = q.pop()
    check[cur] = 1
    cnt += 1
    jump_left = cur - stones[cur]
    jump_right = cur + stones[cur]
    if jump_left >= 0 and check[jump_left] == 0 :
        q.append(jump_left)
    if jump_right <N and check[jump_right] == 0 :
        q.append(jump_right)

print(cnt)


