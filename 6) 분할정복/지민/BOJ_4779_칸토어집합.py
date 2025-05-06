
# N=int(input())

def kan(l,n):
    if l=='-':
        return kan(l,n)
    else:
        kan(l,n)=kan(l,n//3)+(' '*n//3)+kan(n//3)
    
while True:
    N=int(input())
    l='-'*(3**N)
    kan(l,N)

