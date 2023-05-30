# Binarysearch Algorithm

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# example usage  
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Target value {target} found at index {result}")
else:
    print(f"Target value {target} not found in array")