import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N=int(input())
    price=list(map(int, input().split()))
    # (9-5)+(9-3)=10
    # (3-1)+(2-1)+(2-1)=5
    
    max=0 # price중 최대
    result=0 # 최대이익

    for i in price: #[1,1,3,1,2]
        if price[i]>max:
            max=price[i]
        else:
            result+=max-price[i]

        print(result)