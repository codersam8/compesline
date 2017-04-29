# http://practice.geeksforgeeks.org/problems/generate-binary-string/0
test_cases = int(input().strip())
# be careful when working with mutable objects in recursion
def prn_str(ip_str, idx):
    # copying array here instead of at the
    # place of calling. needed only once
    ip_str = ip_str[:]
    # print(ip_str, idx)
    if idx == len(ip_str):
        print(''.join(ip_str))
    elif ip_str[idx] == '?':
        ip_str[idx] = '0'
        prn_str(ip_str, idx + 1)
        ip_str[idx] = '1'
        prn_str(ip_str, idx + 1)
    else:
        prn_str(ip_str, idx + 1)
        
for a_tc in range(test_cases):
    ip_str = input().strip()
    ip_str = list(ip_str)
    # print('*' * 80)
    # print('ip_str', ip_str)
    
    prn_str(ip_str, 0)

    
