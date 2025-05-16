import sys
input=sys.stdin.readline

n=int(input())  # 사진틀의 개수
m=int(input())  # 전체 학생의 총 추천 횟수

rec=list(map(int,input().split())) # 추천받은 학생

frame=[] # 사진 틀
cnt=0 # 추천 수

for i in range(m):
    student=rec[i]

    if student in frame:  # 추천받은 학생이 사진틀에 있으면
        cnt+=1

    else:   # 사진틀에 없는데
        if len(frame)>=n: # 사진틀이 꽉차있으면
            # 삭제할 학생 찾아서

            # frame.remove(student) # 학생 삭제
            # 추천 수 초기화

            # frame.append(student) # 학생 추가
            # 추천 수 증가


# frame.sort()  # 정렬
# print(frame)
