# Quicksort Algorithm

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    equal = []
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    return quicksort(left) + equal + quicksort(right)

print(quicksort([3,4,8,10,9,2,1,5,7,6]))