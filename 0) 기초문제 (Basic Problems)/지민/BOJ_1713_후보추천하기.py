import heapq
import sys

input=sys.stdin.readline

N=int(input())
R=int(input())
# Num=list(map(int,input().split()))

# q=[]
# r=0
# t=0

# for n in range(R):
#     for i in Num:
#         t+=1
#         if i in q:
#             r+=1
#             heapq.heappush(q,[r,t,i])
#         else :
#             r+=1
            
#             heapq.heappush(q,[r,t,i])
#         if len(q)>N:
            
#             heapq.heappop(q)
# print(q)

recs = list(map(int, input().split()))  # 추천받은 학생 목록
frames = []  # 사진틀에 현재 올라간 학생 정보: [{'id': x, 'rec': y, 'time': z}]
student_info = {}  # 학생 번호 -> {'rec': 추천 수, 'time': 게시 시간}

time = 0
for student in recs:
    time += 1
    if student in student_info:
        # 이미 게시된 학생이면 추천수만 증가
        student_info[student]['rec'] += 1
    else:
        # 사진틀에 자리가 없다면 하나 제거
        if len(student_info) >= N:
            # 추천 수 가장 적고, 시간 가장 오래된 학생 찾기
            to_remove = sorted(student_info.items(), key=lambda x: (x[1]['rec'], x[1]['time']))[0][0]
            del student_info[to_remove]
        
        # 새 학생 게시
        student_info[student] = {'rec': 1, 'time': time}

# 남아 있는 학생들 오름차순 출력
print(' '.join(map(str, sorted(student_info.keys()))))