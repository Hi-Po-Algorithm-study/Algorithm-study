import sys
input = sys.stdin.readline

noti_time_str = input().strip()

noti_time_h = int(noti_time_str[0]) * 10 + int(noti_time_str[1])
noti_time_m = int(noti_time_str[3]) * 10 + int(noti_time_str[4])

N = int(input())
doNotDisturb_start = []
doNotDisturb_end = []

for i in range(N):
    doNotDisturb_str = input().strip()
    doNotDisturb_start_h = int(doNotDisturb_str[0]) * 10 + int(doNotDisturb_str[1])
    doNotDisturb_start_m = int(doNotDisturb_str[3]) * 10 + int(doNotDisturb_str[4])

    doNotDisturb_end_h = int(doNotDisturb_str[6]) * 10 + int(doNotDisturb_str[7])
    doNotDisturb_end_m = int(doNotDisturb_str[9]) * 10 + int(doNotDisturb_str[10])

    doNotDisturb_start.append((doNotDisturb_start_h,doNotDisturb_start_m))
    doNotDisturb_end.append((doNotDisturb_end_h,doNotDisturb_end_m))

for i in range(N):
    start_h, start_m = doNotDisturb_start[i]
    end_h, end_m = doNotDisturb_end[i]
    
    if start_h < end_h: # 날 안넘어감
        if noti_time_h > start_h or (noti_time_h == start_h and noti_time_m >= start_m):
            # 알람 시간이 방해금지 시작보다 크고
            if noti_time_h < end_h or (noti_time_h == end_h and noti_time_m < end_m):
                # 알람 시간이 방해금지 종료보다 작으면
                
                noti_time_h = end_h
                noti_time_m = end_m
    else: # 날 넘어감
        if noti_time_h > start_h or (noti_time_h == start_h and noti_time_m >= start_m):
            noti_time_h = end_h
            noti_time_m = end_m  

        
if noti_time_h >= 10 and noti_time_m >= 10:
    print(noti_time_h,":", noti_time_m, sep="")
elif noti_time_h >=10 and noti_time_m < 10:
    print(noti_time_h,":","0",noti_time_m, sep="")
elif noti_time_h <10 and noti_time_m >= 10:
    print('0', noti_time_h,":",noti_time_m, sep="")
else:
    print('0',noti_time_h,":","0",noti_time_m, sep="")
    
