import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
num = set(map(int,sys.stdin.readline().split()))
sensor = []
if N == 1 :
    print(0)
else :
    for i in num :
        sensor.append(i)
    sensor.sort()
    check = [0 for _ in range(len(sensor))]
    for i in range(len(sensor)-1) :
        check[i] = sensor[i+1] - sensor[i]

    check.sort()
    if K != 1 :
        for i in range(1,K) :
            check[len(check)-i] = 0

    print(sum(check))
        


