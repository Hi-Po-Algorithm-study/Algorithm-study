noti_time=input()
N=int(input())
D=[]
S=[]
E=[]
for _ in range(N):
    d=input()
    l=d.split("~")
    start=l[0]
    end=l[1]
    S.append(start)
    E.append(end)

    # print(l)
    D.append(l)
initial=noti_time.split(":")
N_HH=int(initial[0])
N_MM=int(initial[1])

# # for i in range(N):
# print(Time)
# for i in Time:
#     Si.split

# def time():
#     for _ in range(24):
        