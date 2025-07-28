from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

deck = deque([])
ans = []

for i in range(N):
    deck.append(i+1)

while len(deck) > 1:
    k = deck.popleft()
    ans.append(k)
    k2 = deck.popleft()
    deck.append(k2)

l = deck.pop()
ans.append(l)

print(*ans)