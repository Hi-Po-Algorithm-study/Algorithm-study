import sys
N, M = map(int, sys.stdin.readline().split())

long = list(map(int, sys.stdin.readline().split()))
left = max(long)-1
right = sum(long)
min = right//M  
cnt = 1
while(left<right) :
    if (N==M) :
        print(left+1)
        break

    mid = (left + right) // 2
    
    if(min<mid) :
        right = mid
    else :
        left = mid
    cnt+=1
    if(cnt==M) :
        print(mid)
        break

