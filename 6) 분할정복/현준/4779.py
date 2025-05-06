import sys
input = sys.stdin.readline

# 이거 뭐 파일의 끝에서 멈추는거 있었는데 기억 안남
while True: 
    num = int(input()) 
    i = 0
    ans = '-'
    while i != num:
        mult = 1
        for _ in range(i):
            mult = mult * 3
        ans = ans + " " * mult + ans
        i += 1     
    print(ans)