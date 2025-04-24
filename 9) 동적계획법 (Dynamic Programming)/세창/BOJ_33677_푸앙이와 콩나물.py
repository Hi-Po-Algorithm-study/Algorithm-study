import sys
import heapq
input=sys.stdin.readline

def day_water(n):

    if n==0:
        return 0,0
    
    visit={}  # 방문 콩나무 길이 저장(day, water)

    heap=[]

    heapq.heappush(heap, (0,0,0))
    visit[0]=(0,0) 
    # 0일차에 0물, 0콩나무길이

    while heap:
        day,water,length=heapq.heappop(heap)   # 최소 일수,최소 물 사용량,콩나무 길이 pop

        if length==n:
            return day,water
        
        # 물주는 방식 3가지 
        for use_water in [1,3,5]:
            if use_water==1: new_length=length+1
            if use_water==3: new_length=length*3
            if use_water==5: new_length=length*length
        


############################################################################################

n=int(input())

day,water=day_water(n) # 최소 일수 & 최소 물 사용량

print(day,water)