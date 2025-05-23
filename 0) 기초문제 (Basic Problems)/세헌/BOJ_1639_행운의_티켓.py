import sys
num = list(map(int,sys.stdin.readline().strip()))
l = len(num)
cnt = (l - (l%2))//2
ans = 0
check = 100
for i in range(cnt,-1,-1) :
    n = l - (i*2) + 1
    for j in range(n) :
        s1 = 0
        s2 = 0
        lists = num[j:(i*2)-j]
        mid = len(lists)//2 + j
        for k in range(0,mid) :
            s1 += lists[k]
            s2 += lists[k+mid]
        if s1 == s2 :
            check = -1
            break
    if check < 0 :
        ans = i
        break
print(ans*2)