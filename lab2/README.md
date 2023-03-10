# Algorithm Analysis

## Subject
Study and empirical analysis of sorting algorithms. Analysis of quickSort, mergeSort, heapSort, pigeonHoleSort

## Tasks
1. Implement the algorithms listed above in a programming language
2. Establish the properties of the input data against which the analysis is performed
3. Choose metrics for comparing algorithms
4. Perform empirical analysis of the proposed algprithms 
5. Make a graphical presentation of the data obtained
6. Make a conclusion on the work done

**Pigeonhole sorting** is a sorting algorithm that is suitable for sorting lists of elements where the number n of elements and the length N of the range of possible key values are approximately the same. It requires O(n + N) time. It is similar to counting sort, but differs in that it "moves items twice: once to the bucket array and again to the final destination [whereas] counting sort builds an auxiliary array then uses the array to compute each item's final destination and move the item there."

The pigeonhole algorithm works as follows:

1. Given an array of values to be sorted, set up an auxiliary array of initially empty "pigeonholes", one pigeonhole for each key in the range of the keys in the original array.
2. Going over the original array, put each value into the pigeonhole corresponding to its key, such that each pigeonhole eventually contains a list of all values with that key.
3. Iterate over the pigeonhole array in increasing order of keys, and for each pigeonhole, put its elements into the original array in increasing order