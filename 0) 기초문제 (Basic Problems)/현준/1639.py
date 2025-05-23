import sys
input = sys.stdin.readline

S = list(map(int, input().strip()))

length = len(S)
ans = 0

for l in range(length, 1, -1):
    if l%2 == 0 :
        for i in range(length - l + 1):
            startIndex = i
            endIndex = i + l - 1
            mid = (startIndex + endIndex) // 2
            leftS = 0
            rightS = 0
            # print(l)
            # print(startIndex, mid, endIndex)
            for j in range(startIndex, mid+1):
             
                leftS += S[j]
            for j in range(mid+1 , endIndex+1):
                rightS += S[j]
            if leftS == rightS and leftS != 0:
                
                ans = max(ans, l)
    

    # if ans != 0:
    #     break

print(ans)

