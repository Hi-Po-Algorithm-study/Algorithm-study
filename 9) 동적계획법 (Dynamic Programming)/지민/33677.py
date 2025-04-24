import math

N=int(input())

arr=[1,1,1] + [0]*(N-3)

for i in range(N):
    I=math.sqrt(i)

    if i %3 !=0 and ((I*I)-i)!=0.0:
        arr[i]=arr[i-1]+1

    elif i%3==0 and  ((I*I)-i)!=0.0:
        arr[i]=i//3+3

    elif i%3!=0 and  ((I*I)-i)==0.0:
        arr[i]=round(math.sqrt(i)+5)
        
        
    else:
        arr[i]=round(min(math.sqrt(i)+5,i//3+3))
        


print(arr)

        
        
#         math.sqrt(i) != 

# I=math.sqrt(N)
# print((I*I)-16)