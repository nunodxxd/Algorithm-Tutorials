# Mergesort

Merge Sort is a divide and conquer algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array. It works by recursively breaking down a problem into two or more sub-problems of the same or related type until these become simple enough to be solved directly.

One of the main advantages of merge sort is that it has a time complexity of O(n log n), which means it can sort large arrays relatively quickly. It is also a stable sort, which means that the order of elements with equal values is preserved during the sort1.

# Code Explanation

The merge_sort function takes an input array arr and recursively divides it into two halves until the base case is reached where the length of the array is less than or equal to 1. At this point, the function returns the array itself.

The two halves of the array are then sorted recursively by calling the merge_sort function on each half. Once both halves are sorted, they are merged together using the merge function.

The merge function takes two sorted arrays left and right as input and merges them into a single sorted array. This is done by comparing the first elements of both arrays and appending the smaller element to a new merged array. The index of the array from which the smaller element was taken is then incremented. This process is repeated until one of the arrays is exhausted.

Once one of the arrays is exhausted, any remaining elements in the other array are appended to the merged array. The final merged array is then returned.

In this example, an unsorted list my_list is defined and passed to the merge_sort function. The sorted list is then stored in a variable sorted_list and printed to the console.


