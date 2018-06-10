
def selection_sort(list,n):
    for i in range(len(list)):

        for j in range(i,len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

lst = [2,4,6,7,1,9,3]
sorting = selection_sort(lst,len(lst))
print(sorting)