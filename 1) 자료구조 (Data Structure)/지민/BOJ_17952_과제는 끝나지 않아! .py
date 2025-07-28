# # N=int(input())
# # L=[]

# # for _ in range(N):
# #     m=input()

# #     if m!="0":
# #         t=m.split(" ")
# #         task, score, time = int(t[0]), int(t[1]),int(t[2])
# #         L.append([score, time])
# #     else:
# #         L.append(int(m))
# # # print(L)

# # Stack=[]
# # cnt=0
# # for i in range(N):
# #     if L[i] !=0:
# #         # print(L[i][1]-1)
# #         Stack.append([L[i][0],L[i][1]-1])
# #     else:

# #         #pop하고 스택에 푸쉬해야함
# #         if Stack[i-1][1]-1 >0:
# #             Stack.append([Stack[i-1][0], Stack[i-1][1]-1])
# #         elif  Stack[i-1][1]-1==0:
# #         # if  (L[i][1]-1) ==0:
# #             ti=Stack.pop(i-1)
# #             print(ti)
# #             # cnt+=ti[i][0]
# #         else :
# #             break

# # print(cnt)
# #         # else:
# #         #     Stack.append([L[i-1][0],L[i-1][1]-1])
# #         # print(Stack)   
    
# N=int(input())

# work=[]
# score=0

# for _ in range(N):
#     g=input().strip()
#     if g=='0':
#         A,T=work.pop()
#         else:
#             score+=A