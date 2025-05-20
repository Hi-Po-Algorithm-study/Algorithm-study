import sys
# N=int(input())

N=sys.stdin.readlines()

def kan(n):
    if n==0:
        return '-'
    prev=kan(n-1)
    return prev+(' '*(3**(n-1)))+prev


for i in N:
    i = i.strip()
    if not i:
        continue
    n = int(i)
    print(kan(n))
    

