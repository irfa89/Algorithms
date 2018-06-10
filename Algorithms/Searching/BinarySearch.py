def recurBinarySearch(lis, l, r, x):
    if r >= l:
        m = l + (r-l)//2

        if lis[m] == x:
            return m
        elif lis[m] > x:
            return recurBinarySearch(lis, l, m-1, x)
        else:
            return recurBinarySearch(lis, m+1, r, x)
    else:
        return -1


def iterBinarySearch(lis, l, r, x):
    while l <= r:
        m = l + (r-l)//2
        if lis[m] == x:
            return m
        elif lis[m] < x:
            l = m +1
        else:
            r = m -1
    return -1


x = 10
lis = [2,4,6,8,10]

res = recurBinarySearch(lis, 0, len(lis)-1, x)

if res != -1 :
    print("present at index : {0}".format(res))
else :
    print("not present in the list")