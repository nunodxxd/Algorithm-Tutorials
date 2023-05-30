# Heapsort

Heapsort is a comparison-based sorting algorithm that works by dividing the input into a sorted and an unsorted region. It iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.

The improvement consists of using a heap data structure rather than a linear-time search to find the maximum. The heap data structure is an array object that can be viewed as a nearly complete binary tree. Each node of the tree corresponds to an element of the array.

The algorithm works in two phases. In the first phase, the array is transformed into a max heap. The second phase repeatedly extracts the maximum element from the heap and restores the heap property.

# Code Explanation

The heapify function takes three parameters: the array arr, the size of the heap n, and the index of the current node i. It is responsible for maintaining the heap property, which means that the value of each node is greater than or equal to the values of its children.

Inside the heapify function, we initialize largest as the current node i, representing the root of the subtree. We also calculate the indices of the left and right child nodes.

We then compare the value of the left child with the root node. If the left child is greater, we update largest accordingly.

Next, we compare the value of the right child with the node at largest. If the right child is greater, we update largest again.

If largest is not equal to i, it means that one of the child nodes is greater than the root. In this case, we swap the values of the root and the node at largest. This ensures that the largest value is at the root position.

After the swap, we recursively call heapify on the affected child node to maintain the heap property throughout the entire heap.

The heap_sort function takes an array arr as a parameter and performs the heapsort algorithm on it.

Inside heap_sort, we initialize n as the length of the array.

We start by building a max heap from the input array. We iterate from the last non-leaf node (which is at index n // 2 - 1) to the first node (index 0) and perform heapify on each node. This step ensures that the array satisfies the heap property.

Once the max heap is built, we start extracting elements from the heap. We iterate from the last element (index n-1) to the second element (index 1).

In each iteration, we swap the root element (which is the maximum value in the heap) with the last element in the heap. This moves the maximum element to its correct sorted position at the end of the array.

After the swap, we decrease the size of the heap by 1 and call heapify on the root node to restore the heap property.

Finally, when the loop ends, the array is sorted in ascending order.
