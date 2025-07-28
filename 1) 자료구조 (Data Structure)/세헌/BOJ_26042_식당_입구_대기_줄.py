import sys
from collections import deque
T = int(sys.stdin.readline())
lists = deque()
for _ in range(T) :
    N = sys.stdin.readline().strip()
    if N[0]=='1' :
       a,b = N.split()
       lists.append(int(b))
    else :
        lists.append(N)
max = 0
min = sys.maxsize
line = deque()
while(lists) :
    n = lists.popleft()
    if n == '2' :
        if max < len(line) :
            max = len(line)
            min = line[max-1]
        elif max == len(line) :
            if min > line[max-1] :
                min = line[max-1]
        line.popleft()
    else :
        line.append(n)
if max < len(line) :
    max = len(line)
    min = line[max-1]
elif max == len(line) :
    if min > line[max-1] :
        min = line[max-1]
print(max,min)