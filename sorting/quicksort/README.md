# Quicksort

The Quicksort algorithm follows a "divide and conquer" approach, where it repeatedly partitions the array based on a chosen pivot element and recursively sorts the subarrays. The efficiency of Quicksort depends on the choice of pivot and the input data, but on average, it has a time complexity of O(n log n), where n is the number of elements in the array.

# Code Explanation 

The quicksort function takes an array arr as input and checks if the length of the array is less than or equal to 1. If so, it means the array is already sorted or contains only one element, so we can simply return the array.

We select the pivot element by taking the element at the middle index of the array (len(arr) // 2). This is a simple choice, but other pivot selection strategies can also be used.

We initialize three empty lists: left, right, and equal. These lists will store elements from the original array based on their relationship to the pivot.

We iterate through each element (num) in the original array arr and compare it to the pivot. Depending on the comparison result, we append the element to the appropriate list (left, right, or equal).

If num is less than the pivot, we append it to the left list.
If num is greater than the pivot, we append it to the right list.
If num is equal to the pivot, we append it to the equal list.
By the end of this loop, the original array has been partitioned into three parts: elements less than the pivot (left), elements greater than the pivot (right), and elements equal to the pivot (equal).

We recursively call the quicksort function on the left and right subarrays. The recursive calls continue until the base case is reached (when the length of the subarray is less than or equal to 1).

Finally, we concatenate the sorted left subarray, the equal subarray (since all elements are already in their correct position), and the sorted right subarray using the + operator. This gives us the sorted array for the current recursion step.

