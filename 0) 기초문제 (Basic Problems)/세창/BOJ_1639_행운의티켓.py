s=input()

n=len(s)
max_len=0

for left in range(n):
    for right in range(left+1,n+1,2):
        mid=(left+right)//2
        sum_left=sum(map(int,s[left:mid]))
        sum_right=sum(map(int,s[mid:right]))

        if sum_left==sum_right:
            max_len=(right-left)+1

print(max_len)