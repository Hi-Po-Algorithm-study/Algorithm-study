import sys
N = int(sys.stdin.readline())
Ah = 0
Am = 0
Bh= 0
Bm = 0
Goal = 0
after_H = 0
after_M = 0
after_T = '0'
after_g = 0
for i in range(N) :
    print('A',Ah,Am)
    print('B',Bh,Bm)
    team,time = sys.stdin.readline().split()
    H, M = map(int, time.split(':'))
    h = 0
    m = 0
    if i == N-1 :
        if M>0 :
            m = 60 - M
            h = 47 - H
        else :
            h = 48 - H

        if Goal>0:
            Ah += h 
            Am += m 
            if Am>=60 :
                Am -= 60
                Ah += 1
        elif Goal<0 :
            Bh += h 
            Bm += m 
            if Bm>=60 :
                Bm -= 60
                Bh += 1
    
    if i == 0 :
        after_H = H 
        after_M = M
        after_T = team
        after_G = Goal

    elif after_T !='0' :
        m = M - after_M
        h = H - after_H
        if m<0 :
            m += 60
            h -= 1

        if after_G>0 :
            Ah += h 
            Am += m 
            if Am>=60 :
                Am -= 60
                Ah += 1
        elif after_G<0 :
            Bh += h 
            Bm += m 
            if Bm>=60 :
                Bm -= 60
                Bh += 1
        after_G = Goal
        after_H = M 
        after_M = M 
        after_T = team


print(Ah,Am)
print(Bh,Bm)

