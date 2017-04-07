# http://practice.geeksforgeeks.org/problems/check-if-a-number-can-be-expressed-as-xy/0
test_cases = int(input().strip())
# essentially solved using hashmap
for a_tc in range(test_cases):
    
    numbr = int(input().strip())
    all_factors = {}
    divsr = 2
    pow_psbl = True
    if numbr == 1:
        print(1)
        pow_psbl = False
    while numbr > 1:
        if numbr % divsr == 0:
            numbr /= divsr
            if divsr in all_factors:
                all_factors[divsr] += 1
            else:
                all_factors[divsr] = 1
        else:
            divsr += 1

    times_repeated = list(all_factors.values())
    val = None
    if len(times_repeated) > 0:
        val = times_repeated[0]

    if val == 1:
        print(0)
        pow_psbl = False
    else:
        for a_val in times_repeated:
            if val != a_val:
                pow_psbl = False
                print(0)
                break

    if pow_psbl:
        print(1)
        
