N=int(input())
total_MM=48
total_SS=00

goal=[]

for _ in range(N):
    l=input()
    L=l.split()

    team=int(L[0])
    MM_SS=L[1]
    time=MM_SS.split(":")
    MM=int(time[0])
    SS=int(time[1])

    goal.append((team, MM, SS))


for i in range(N):
    goal.pop()
    if N==1:
        if total_SS-SS<0:
            win_SS=60-SS
            win_MM=total_MM-MM-1
        else :
            win_SS=SS
            win_MM=total_MM-MM
        if team==1:
            print(f"{win_MM}:{win_SS}0")
            print("00:00")
        else:
            print("00:00")
            print(f"{win_MM}:{win_SS}0")
    else:
        

# team_1
# team_2

# for i in range(N):
