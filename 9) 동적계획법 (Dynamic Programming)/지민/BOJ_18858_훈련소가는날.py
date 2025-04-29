import sys

div = 998_244_353

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    before = [[0] * 3 for _ in range(M + 1)]
    now = [[0] * 3 for _ in range(M + 1)]

    for m in range(1, M + 1):
        before[m][1] = 1

    for n in range(1, N):
        sum_ = 0
        for m in range(M, 0, -1):
            sum_ = (sum_ + before[m][0] + before[m][1]) % div
            now[m-1][0] = sum_

        now[1][1] = (before[1][0] + before[1][1] + before[1][2]) % div
        sum_ = now[1][1] % div

        for m in range(2, M + 1):
            now[m][2] = sum_
            now[m][1] = (before[m][0] + before[m][1] + before[m][2]) % div
            sum_ = (sum_ + now[m][1]) % div

        before = [row[:] for row in now]
        now = [[0] * 3 for _ in range(M + 1)]

    answer = 0
    for m in range(1, M + 1):
        answer = (answer + before[m][0] + before[m][1] + before[m][2]) % div

    print(answer)

if __name__ == "__main__":
    main()