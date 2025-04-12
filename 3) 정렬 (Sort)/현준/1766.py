import sys
import heapq  # 우선순위 때문에 힙 사용

# from collections import deque # 처음에 큐로 하려 했으나 우선순위 실패

input = sys.stdin.readline

N, M = map(int, input().split())  # 문제수, 정보 수
dic = {i: [] for i in range(1, N + 1)}  # 그래프
indegree = [0 for _ in range(N + 1)]  # 진입차수

priorityQ = []  # 우선 순위 큐
answer = []  # 결과값 저장

for _ in range(M):  # 그래프, 진입차수 저장
    first, second = map(int, input().split())
    dic[first].append(second)
    indegree[second] += 1


for i in range(1, N + 1):  # 먼저 진입차수가 0인 놈들 힙에 넣기
    if indegree[i] == 0:
        heapq.heappush(priorityQ, i)


while priorityQ:  # 큐에 남아있으면 반복

    cur = heapq.heappop(priorityQ)  # 이번에 풀 문제
    answer.append(cur)

    for next in dic[cur]:  # 딕셔너리 확인해서 진입차수 줄여 주기
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(priorityQ, next)


print(*answer)
