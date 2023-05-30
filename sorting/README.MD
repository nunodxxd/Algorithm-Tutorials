# Quicksort vs Heapsort vs Merge Sort

This README.md file provides an overview of three popular sorting algorithms: Quicksort, Heapsort, and Merge Sort. It explains the differences between them and includes visual elements to help understand their operations.

## Quicksort

Quicksort is a divide-and-conquer algorithm that follows the divide-and-conquer paradigm. It works by selecting a pivot element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted. The steps involved in the Quicksort algorithm are as follows:

1. Select a pivot element from the array.
2. Reorder the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it. This step is called partitioning.
3. Recursively apply the above steps to the sub-arrays of elements less than and greater than the pivot.
4. Combine the sorted sub-arrays to get the final sorted array.

Visualization of Quicksort:

![Quicksort Visualization](quicksort.gif)

## Heapsort

Heapsort is also a comparison-based sorting algorithm that uses a binary heap data structure. It starts by building a max heap from the input array and then repeatedly extracting the maximum element from the heap and placing it at the end of the array. The steps involved in the Heapsort algorithm are as follows:

1. Build a max heap from the input array.
2. Swap the root (maximum element) with the last element in the heap.
3. Remove the last element from the heap (reducing the heap size by 1) and heapify the root to maintain the heap property.
4. Repeat steps 2 and 3 until the heap is empty.
5. The sorted array is obtained by reversing the elements obtained in step 2.

Visualization of Heapsort:

![Heapsort Visualization](heapsort.gif)

## Merge Sort

Merge Sort is another divide-and-conquer algorithm that works by recursively dividing the input array into two halves, sorting them, and then merging the sorted halves. The steps involved in the Merge Sort algorithm are as follows:

1. Divide the input array into two halves.
2. Recursively sort the two halves.
3. Merge the sorted halves to obtain the final sorted array.

Visualization of Merge Sort:

![Merge Sort Visualization](merge_sort.gif)

## Comparison

Here are some key differences between these sorting algorithms:

- Quicksort has an average and best-case time complexity of O(n log n), but its worst-case time complexity is O(n^2) when the pivot selection is unbalanced. Heapsort and Merge Sort have a guaranteed worst-case time complexity of O(n log n).
- Quicksort is an in-place sorting algorithm, meaning it doesn't require additional memory proportional to the input size. Heapsort and Merge Sort require additional memory for auxiliary data structures.
- Heapsort is not a stable sorting algorithm, meaning it does not necessarily preserve the relative order of equal elements. Quicksort and Merge Sort can be implemented as stable sorting algorithms.
- Quicksort is widely used in practice due to its average-case performance and efficient partitioning. Heapsort is useful when a guaranteed worst-case time complexity is required. Merge Sort is often used when stability and worst-case performance are desired.

In conclusion, all three sorting algorithms have their own strengths and are suitable for different scenarios. Understanding their differences and characteristics can help in selecting the most appropriate sorting algorithm for a given situation.
