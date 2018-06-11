
def insertion_sort(list):
    for i in range (1,len(list)):
        key = list[i]
        j = i-1
        while j>= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

    return list

lst = [42,3,5,2,67,92,56,1]
sort_lst = insertion_sort(lst)
print(sort_lst)