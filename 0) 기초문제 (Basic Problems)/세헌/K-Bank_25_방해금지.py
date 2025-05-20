import sys
H,M = map(int, sys.stdin.readline().split(':'))
N = int(sys.stdin.readline())
nh =[] 
nm = [] 
check = [0] * N
for i in range(N) :
    s,e = sys.stdin.readline().split('~')
    sh,sm = map(int, s.split(':'))
    eh,em = map(int, e.split(':'))
    nh.append([sh,sm])
    nm.append([eh,em])
    if sh>=eh and sm>em :
        check[i] = 1
cnt = 0
h = H
m = M
ans = True

while(ans) :
    for i in range(N) :       
        if (nh[i][0]<h or(nh[i][0]==h and  nh[i][1]<=m)) :
            if check[i]==0 and (nm[i][0]>h or(nm[i][0]==h and  nm[i][1]>m)) :
                h=nm[i][0]
                m=nm[i][1]
                ans = True
                break
            elif check[i]==1:
                cnt = 1
                h=nm[i][0]
                m=nm[i][1]
                ans = True
                break
        else :
            ans =False
    if cnt==1 and (h>H or (h==H and m>M)) :
        break


if cnt==1 and (h>H or (h==H and m>=M)) :
    print('impossible')
else :
    print(h,':',m)



