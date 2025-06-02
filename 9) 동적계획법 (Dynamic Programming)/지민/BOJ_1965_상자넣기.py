n=int(input())

box=list(map(int,input().split()))

lst=[]
min=0
for i in range(n):
    for j in range(i,n+1):

        if box[i]<box[j]:
            min=j
            if box[j]-box[i] < box[j+1]-box[i]:
                min=j+1
            
            print(min)
                

            
        