def linear_search(arr, target):
    for i in range(len(arr)):
        if arr [i] == target:
            return i
    return -1

list = [1, 3, 5, 7, 9]
result = linear_search(list, 5)
print (result)