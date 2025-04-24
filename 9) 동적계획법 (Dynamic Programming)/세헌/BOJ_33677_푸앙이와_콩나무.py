import sys
import math
N = int(sys.stdin.readline())

dp_day = [sys.maxsize] * (N+5)
dp_water = [sys.maxsize] * (N+5)
dp_day[0] = 0
dp_water[0] = 0
dp_day[1] = 1
dp_water[1] = 1
if N > 1 :
    for i in range(2,N+1) :
        h = 0
        if math.sqrt(i)%1==0 :
            h = int(math.sqrt(i))
            dp_day[i] = dp_day[h] + 1
            dp_water[i] = dp_water[h] + 5

        if i%3 == 0 :
            h = i//3
            if dp_day[i] > dp_day[h] + 1 :
                dp_day[i] = dp_day[h] + 1
                dp_water[i] = dp_water[h] + 3
            elif dp_day[i] == dp_day[h] + 1 :
                dp_water[i] = min(dp_water[i], dp_water[h] + 3)
        
        d = dp_day[i-1] + 1
        if dp_day[i] > d :
            dp_day[i] = d
            dp_water[i] = dp_water[i-1] + 1
        elif dp_day[i] == d :
            dp_water[i] = min(dp_water[i], dp_water[i-1] + 1)

print(dp_day[N], dp_water[N])
