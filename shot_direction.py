# http://practice.geeksforgeeks.org/problems/shortest-direction/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    directions = input().strip()
    dir_count = {
        'N': 0,
        'S': 0,
        'E': 0,
        'W': 0
    }

    for a_dir in directions:
            dir_count[a_dir] +=1
    # print(dir_count)
    short_dir = ''
    if 'E' in dir_count and 'W' in dir_count:
        ew = dir_count['E'] - dir_count['W']

        if ew > 0:
            short_dir = 'E' * ew
        else:
            short_dir = 'W' * -ew
    # print(short_dir)
    if 'N' in dir_count and 'S' in dir_count:
        ns = dir_count['N'] - dir_count['S']
        # print(ns)
        if ns > 0:
            short_dir += 'N' * ns
        else:
            short_dir += 'S' * -ns
    short_dir = sorted(short_dir)
    short_dir = ''.join(short_dir)
    print(short_dir)
    
    
