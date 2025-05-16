import heapq

N=int(input())
R=int(input())
Num=list(map(int,input().split()))

q=[]
r=0
t=0
# while q:
for n in range(R):
    # heapq.heappush(q,[0,0,0])
    for i in Num:
        t+=1
        if i in q:
            r+=1
            heapq.heappush(q,[r,t,i])
        else :
            r+=1
            
            heapq.heappush(q,[r,t,i])
        if len(q)>N:
            
            heapq.heappop(q)
print(q)


    # if i in photo:


# for i in Num:
#     lst.append(i)
#     for ii in range(R):
#         if lst:
            
#             heapq.heappush(ii,t)



# cnt=[]
# for i in Num:
#     cnt.append(Num.count(i))
#     if 
# print(cnt)