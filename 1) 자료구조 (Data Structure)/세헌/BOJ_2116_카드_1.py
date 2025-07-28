import sys
from collections import deque 
N = int(sys.stdin.readline())
card = deque()
for i in range(1,N+1) :
    card.append(i)
cnt =True
result = []
while(card) :
    if cnt :
        result.append(card.popleft())
        cnt = False
    else :
        n = card.popleft()
        card.append(n)
        cnt =True

print(*result)