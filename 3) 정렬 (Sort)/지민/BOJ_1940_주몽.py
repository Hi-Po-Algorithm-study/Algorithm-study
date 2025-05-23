import sys
input=sys.stdin.readline

N=int(input())
M=int(input())
lst=list(map(int,input().split()))

cnt=0

for i in lst:
    for j in lst:
        if i!=j and i+j==M:
            # print(i)
            lst.remove(i)
            lst.remove(j)
            cnt+=1
        # else:
        #     break
            print((i,j))
print(cnt)

# for i in range(N-1):
#     for j in range(N-1,0,-1):

#         if lst[i]+lst[j-1] == M:
#             cnt+=1
#             lst[i]=lst[i+1]
#             lst[j]=lst[j-1]
#         else :
#             lst[i]=lst[i+1]
#         if i==j:
#             break
# print(cnt)

