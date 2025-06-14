import sys

def dfs(n,idx) :
    if n == 6 :
        print(*lotto)

    for i in range(idx,num[0]) :
        lotto.append(lt[i])
        dfs(n+1,i+1)
        lotto.pop()
    


while (True) :
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] <= 6 :
        break
    lt = num[1:]
    lt.sort()
    lotto = []
    dfs(0,0)
    print()



    

