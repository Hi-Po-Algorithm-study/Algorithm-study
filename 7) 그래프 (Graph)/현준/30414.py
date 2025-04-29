import sys
input = sys.stdin.readline

N, P = map(int, input().split()) # N은 산개수, 병사수, P는 시작 산

originHeight = list(map(int, input().split()))
chunbaeHeight = list(map(int, input().split()))

visited = [0 for _ in range(N)]
dp = [0 for _ in range(N)]
haveDirt = 0
# dp[now] => 현재 산에서의 최소 비용
# dp[now] = min(dp[이전 노드들]) + 현재 비용

way ={i : [] for i in range(1, N+1)}
for _ in range(N-1):
    m1, m2 = map(int, input().split())
    way[m1].append(m2)
    way[m2].append(m1)
# 정렬은 필요한가?
visited[P-1] = 1

def dfs(P):
    global haveDirt

    if chunbaeHeight[P-1] >= originHeight[P-1]:
        money = chunbaeHeight[P-1] - originHeight[P-1]
        if haveDirt-money >0:
            haveDirt -= money
        else:
            dp[P-1] += money - haveDirt
    else:
        haveDirt += originHeight[P-1] - chunbaeHeight[P-1]

    for next in way[P]:
        if visited[next-1] == 0:
            visited[next-1] = 1
            dfs(next)

dfs(P)
print(dp)
print(haveDirt)
