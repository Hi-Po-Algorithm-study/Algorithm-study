import sys
input = sys.stdin.readline

N, M = map(int, input().split())

minute = list(map(int, input().split()))

start = max(minute) - 1
end = 0
for m in minute:
    end += m

if start == end:
    mid = start
else:
    while start < end:
        if end - start == 1:
            mid = end
            break
        # print("s e", start, end)
        mid = (start + end) // 2
        # print("m", mid)
        count = 1
        blueray = 0
        for a in minute:
            if (blueray + a) <= mid:
                blueray += a
            else:
                count += 1
                blueray = a
        # print("c", count)
        if count <= M:
            end = mid
        else:
            start = mid


print(mid)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

minute = list(map(int, input().split()))

start = 0
end = 0
for m in minute:
    end += m




while start < end:
    if end - start == 1:
        mid = end
        break
    # print("s e", start, end)
    mid = (start + end) // 2
    # print("m", mid)
    count = 1
    blueray = 0
    for a in minute:
        if (blueray + a) <= mid:
            blueray += a
        else:
            count += 1
            blueray = a
    # print("c", count)
    if count <= M:
        end = mid
    else:
        start = mid


print(mid)
