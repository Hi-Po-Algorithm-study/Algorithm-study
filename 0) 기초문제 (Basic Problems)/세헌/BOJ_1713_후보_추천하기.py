import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
reco = list(map(int,sys.stdin.readline().split()))
score = []
std = [0] * 101
photo = [0] * 101
for _ in range(N) :
    heapq.heappush(score, [0,0,0])
for i in range(M) :
    std[reco[i]] += 1
    cur = std[reco[i]]
    if photo[reco[i]] == 0 :
        r,t,s = heapq.heappop(score)
        heapq.heappush(score, [cur,i+1,reco[i]])
        photo[reco[i]] = 1
        photo[s] = 0
        std[s] = 0
    else :
        for j in range(N) :
            r,t,s = heapq.heappop(score)
            if s==reco[i] :
                heapq.heappush(score, [cur,t,s])
                break
            else :
                heapq.heappush(score, [r,t,s])
ans = []
print(*ans)
while score :
    rr,tt,ss = heapq.heappop(score)
    if ss != 0 :
        ans.append(ss)

ans.sort()
print(*ans)
 