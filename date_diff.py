test_cases = int(input().strip())
# print("test cases " + str(test_cases))
month_days = [31, 28, 31, 30, 31, 30,
                           31, 31, 30, 31, 30, 31]

def find_days_before_date(a_date):
    year = a_date[2]
    days = 365 * year
    if a_date[1] <= 2:
        year -= 1
        
    days += (int(year / 4) - int(year / 100) + int(year / 400))

    for a_month in range(a_date[1] - 1):
        days += month_days[a_month]

    days += a_date[0]

    return days
    
for test_case in range(test_cases):
    date1 = input().strip().split(' ')
    date1 = [int(i) for i in date1]
    date2 = input().strip().split(' ')
    date2 = [int(i) for i in date2]
    # print(date1, date2)
    days_before_date1 = find_days_before_date(date1)
    days_before_date2 = find_days_before_date(date2)
    # print(days_before_date1, days_before_date2)
    print(abs(days_before_date2 - days_before_date1))
