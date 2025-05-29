import sys
input = sys.stdin.readline

N = int(input())

before_winner = 0
before_winner_time_min = 0
before_winner_time_sec = 0
winner = 0
# winner_change_time_min = 0
# winner_change_time_sec = 0
team1_min = 0
team1_sec = 0
team2_min = 0
team2_sec = 0
team1_score = 0
team2_score = 0

for i in range(N):
    
    scored_team, scored_time = map(str, input().split())
    scored_time_min, scored_time_sec = scored_time.split(':')
    scored_team = int(scored_team)
    scored_time_min = int(scored_time_min)
    scored_time_sec = int(scored_time_sec)

    if scored_team == 1:
        team1_score += 1
    else:
        team2_score += 1

    if team1_score > team2_score:
        winner = 1
    elif team2_score > team1_score:
        winner = 2
    else:
        winner = 0
    
    if before_winner != winner:

        if before_winner_time_min != 0 and before_winner_time_sec != 0:
            if before_winner == 1:
                team1_min = team1_min + scored_time_min - before_winner_time_min 
                team1_sec = team1_sec + scored_time_sec - scored_time_sec
            elif before_winner == 2:
                team2_min = team2_min + scored_time_min - before_winner_time_min 
                team2_sec = team2_sec + scored_time_sec - scored_time_sec

        before_winner_time_min = scored_time_min
        before_winner_time_sec = scored_time_sec
    

    before_winner = winner
    
if before_winner == 1:
    team1_min = team1_min + 48 - before_winner_time_min 
    team1_sec = team1_sec + 0 - scored_time_sec
elif before_winner == 2:
    team2_min = team2_min + 48 - before_winner_time_min 
    team2_sec = team2_sec + 0 - scored_time_sec


# 출력

if team1_sec < 0:
    team1_min -= 1
    team1_sec += 60
elif team1_sec >= 60:
    team1_min += (team1_sec // 60)
    team1_sec = team1_sec % 60

if team1_min < 10 and team1_sec < 10:
    print('0' , team1_min, ':','0', team1_sec, sep='')
elif team1_min < 10:
    print('0' , team1_min, ':', team1_sec, sep='')
elif team1_sec < 10:
    print(team1_min, ':','0', team1_sec, sep='')
else:
    print(team1_min, ':', team1_sec, sep='')

if team2_sec < 0:
    team2_min -= 1
    team2_sec += 60
elif team2_sec >= 60:
    team2_min += (team2_sec // 60)
    team2_sec = team2_sec % 60

if team2_min < 10 and team2_sec < 10:
    print('0' , team2_min, ':','0', team2_sec, sep='')
elif team2_min < 10:
    print('0' , team2_min, ':', team2_sec, sep='')
elif team2_sec < 10:
    print(team2_min, ':','0', team2_sec, sep='')
else:
    print(team2_min, ':', team2_sec, sep='')

