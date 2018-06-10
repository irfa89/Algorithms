
def bubble_sort(list):
    n = len(list);
    for i in range(len(list)):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

lst = [42,3,5,2,67,92,56,1]
sort_lst = bubble_sort(lst)
print(sort_lst)
