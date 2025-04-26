import sys
input=sys.stdin.readline

#########################################

n,m=int(input())
a=list(map(int,input().split()))

start=max(a) # 강의 중 제일 긴
end=sum(a)   # 강의들의 합

result=end # 최대로 시작

#print(result)

#########################################

while start<=end:
    mid=(start+end)//2
    
    Bluray=1 #블루레이는 일단 최소 1개는 필요

    for i in a:


    if :    
        start=mid+1

    else:            #블루레이 m개 가능
        end=mid-1    #mid 더 줄여서 확인해보기
        result=mid   #정답후보

print(result)