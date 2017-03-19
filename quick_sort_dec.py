arrr = [5,1,4,2,3]
def partition_dec(arrr, begin, end):
    less_bound = begin - 1
    for curr in range(begin, end):
        if arrr[curr] > arrr[end]:
            less_bound += 1
            arrr[less_bound], arrr[curr] = arrr[curr], arrr[less_bound]
    less_bound += 1
    arrr[less_bound], arrr[end] = arrr[end], arrr[less_bound]
    return less_bound
def quick_sort_dec(arrr, begin, end):
    if(begin < end):
        q = partition_dec(arrr, begin, end)
        # print(q)
        quick_sort_dec(arrr, begin, q - 1)
        quick_sort_dec(arrr, q+1, end)
# quick_sort(arrr, 0, len(arrr) - 1)
# print(arrr)
