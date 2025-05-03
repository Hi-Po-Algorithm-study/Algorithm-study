#크레인이 남아있는 박스 중 가장 무거운 박스를 옮길 수 있는지 따짐
# 가장 큰 무게를 드는 크레인이 가장 무거운 박스를 못옮기면 -1
#-1이 아니면 모든 박스를 옮길 수 있음
#지금 선택한 크레인이 남아 있는 박스 중 가장 가벼운 박스를 옮기지 못한다면 continue

import sys
input=sys.stdin.readline

N=int(input())
c_limit=list(map(int,input().split()))
M=int(input())
B_W=list(map(int,input().split()))

c_limit.sort()
B_W.sort()

cnt=0

if B_W[0]>c_limit[0]:
    cnt=-1
else:
    while B_W:
        for i in c_limit:
            if B_W and i<B_W[-1]:
                continue 
            for ii in B_W:
                if i>=ii:
                    B_W.remove(ii)
                    break
        cnt+=1
print(cnt)  

##################################################################

# import heapq

# N=int(input())
# limit=list(map(int,input().split()))
# M=int(input())
# W=list(map(int,input().split()))

# lim=[]
# min_w=[]
# W.sort()
# cnt=0

# for ii in W:
#     heapq.heappush(min_w,ii)


# while min_w:
#     # a=heapq.heappop(min_w)
#     for k in range(N):
#         a=heapq.heappop(min_w)
#         if limit[k]>a :
#             cnt+=0
#         else:
#             print(-1)
#         if len(min_w) ==0:
#             break
        
#     # heapq.heappush(min_w,M)

#     cnt+=1    

# print(cnt)      
