test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    num_of_soldiers = int(input().strip())
    soldiers = input().strip().split(' ')
    soldiers = [int(i) for i in soldiers]
    soldiers = sorted(soldiers)
    min = soldiers[0]
    max = soldiers[num_of_soldiers - 1]
    for a_soldire in soldiers:
        if min == a_soldire or max == a_soldire:
            num_of_soldiers -= 1
    print(num_of_soldiers)
