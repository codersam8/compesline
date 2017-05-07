# http://practice.geeksforgeeks.org/problems/angle-between-hour-and-minute-hand/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    
    h_m = input().strip().split(' ')
    h, m = [float(i) for i in h_m]

    h_deg = (h * 30) + ((m % 60) * 0.5) % 360
    # print('*' * 80)
    # print('h_deg', h_deg)
    
    m_deg = 6 * (m % 60)
    # print('*' * 80)
    # print('m_deg', m_deg)
    
    angle = abs(h_deg - m_deg)

    if angle > 180:
        angle = 360 - angle
        
    print(int(angle))
