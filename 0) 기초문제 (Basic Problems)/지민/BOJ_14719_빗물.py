H,W=map(int,input().split())
lst=list(map(int,input().split()))

rain=0

# max_h=[]
# max_h.append(lst[0])
# for i in lst:
#     # h=max_h.pop()
#     h=lst[0]
#     if i>h:
#         if i>lst[0] or i>lst[-1]:
#         max_h.append(i)
        
#         print(max_h)
#     else:
#         if len(max_h)!=0:
#             h=max_h.pop()

#         rain+=h-i
# print(rain)

L=[]
for i in range(len(lst)):
    L.append(lst[i])
    if lst[i]<lst[i+1]
