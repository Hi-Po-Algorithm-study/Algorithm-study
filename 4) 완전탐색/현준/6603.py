import sys
input = sys.stdin.readline

def lotto(visit, i, n):

    if i == n:
        return
    
    else:
        visit[i] = 1
        total = 0
        check = []

        for k in range(n):
            if visit[k] == 1:
                check.append(testcase[k+1])

        if len(check) == 6:
            print(*check)
            visit[i] = 0
            lotto(visit, i+1, n)

        else:
            lotto(visit, i+1, n)
            visit[i] = 0
            lotto(visit, i+1, n)


while True:

    testcase = list(map(int,input().split()))

    if testcase[0] == 0:
        break

    else:
        n = testcase[0]
        visited = [0 for _ in range(n)]
        lotto(visited, 0, n)
        print()