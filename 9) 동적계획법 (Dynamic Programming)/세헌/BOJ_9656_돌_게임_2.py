import sys

stone = int(sys.stdin.readline())
name = ['SK', 'CY']

if(stone%4 == 1 or stone%4 == 3) :
    print(name[1])
else :
    print(name[0])



# import sys

# stone = int(sys.stdin.readline())
# name = ['SK', 'CY']

# dp = [-1] * (stone+1)
# dp[1] = 1
# dp[2] = 0
# dp[3] = 1
# if (stone>3) :
#     for i in range(4, stone+1) :
#         dp[i] = dp[i-2]

# print(name[dp[stone]])



