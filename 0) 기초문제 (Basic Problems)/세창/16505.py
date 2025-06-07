import sys
input=sys.stdin.readline

def star(x,y,N):
    if N==1:
        board[x][y]=='*'



    # 별이 세 분류로 나눠짐
    star()  # 왼쪽
    star()  # 오른쪽
    star()  # 아래



n=int(input())

# n마다 보드가 (2^n)x(2^n)
N=2**n
board=[[' ' for _ in range(N)] for _ in range(N)]

star(0,0,N)

print()