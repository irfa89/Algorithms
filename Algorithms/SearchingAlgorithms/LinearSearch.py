
def linearSearch(list, x):
    for i in range(len(list)):
        if list[i] == x :
            return i
    return -1


# An example of implementation of function

arr = [2,4,5,6,7,12,6,7,9,23,45,56,78]

print(" The value is at index : {0}".format(linearSearch(arr,7)))