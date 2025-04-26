import sys
N, M = map(int, sys.stdin.readline().split())

long = list(map(int, sys.stdin.readline().split()))
long.sort()
left = 0
right = N-1

cnt = 1
while(left<right) :
    mid = (left + right) // 2
    l_sum = sum(long[left:mid+1])
    r_sum = sum(long[mid+1:right+1])
    if(l_sum > r_sum) :
        right = mid
    else :
        left = mid + 1
    cnt+=1
    if(cnt==M) :
        print(max(l_sum,r_sum))
        break

