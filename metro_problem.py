test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    station_dir = input().strip().split(' ')
    curr_station = int(station_dir[0])
    direction = station_dir[1]
    
    if curr_station > 11 and direction == 'U':
        print(19 - curr_station + 8)

    elif curr_station > 11 and direction == 'D':
        print(curr_station - 11)

    elif curr_station < 11 and direction == 'U':
        print(11 - curr_station)

    elif curr_station < 11 and direction == 'D':
        print(curr_station + 11)
    else:
        print(0)
