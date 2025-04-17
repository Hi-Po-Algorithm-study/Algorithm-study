import sys
import math
while(True) :
    N = int(sys.stdin.readline())
    if N==0 :
        break
    NN = 2 * N

    arr = [0] * (NN+1)
    arr[1] = 1 
    # 에라 체
    # 1~n까지의 소수를 알고 싶다면, n까지 모든 수의 배수를 다 나눠 볼 필요는 없다. 
    # x*x = n이라고 하면 a*b = n (a<b)에서 a는 x보다 항상 작다.
    # 따라서 x전까지의 배수만 제외 시켜주면 n이하의 소수의 개수를 알 수 있다.
    for i in range(2, int(math.sqrt(NN)) + 1):
       if arr[i] == 1: 
           continue
       for j in range(2 * i, NN + 1, i):
            arr[j] = 1

    cnt = 0
    for i in range(2,NN+1) :
        if i<=N :
            continue
        if arr[i] == 0 :
            cnt+=1

    print(cnt)
        
