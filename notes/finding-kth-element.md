# Finding the k-th largest item in array

** This is just a memo for myself.

## solution 1: sort the array, and array[k - 1]

This takes `O(N log N)`.

```
quicksort(array)

print(array[k-1])
```

But if you add or remove a element or some elements from the array,
we have to re-sort the array.
So, `O(M * N log N)`, `M` represents the number of operation.

------

## solution 2: Use heap sort

The heap is priority queue.
If the heap size is `k`, the k-th largest is always last one.

```python

for val in nums:
  if (len(h) < k):
      heapq.heappush(h, val)
  else:
      heapq.heappushpop(h, val)
```

First, we need to build the heapmap for all elements,
and the heap needs to rebuild itself after changing the elements every time.

`O(log K)` for one time rebuild, and `n` elements.
That's why `O(N log K)`, which is better than `O(N log N)`.

But if `k` is `n/2`, it becomes `O(N log n/2) => O(N log N)`.
Then `M` time operations, `O(MN log N)`.

-----------

## solution 3: use Quick Select

Quick Select algorithm finds the k-th element using Pivot and Partitioning concept like Quick Sort.

In the unsorted array, we just want to know what is the k-th largest element.
Other elements are not related. So, we don't need to sort other elements.

### Algorithm

1. Select a pivot value randomly.
2. Separate the array into two parts, one is smaller than the pivot, and other one is greater than the pivot.
3. Select the partition which has `k-1`.
4. Repeat from step 1 to 3, until we found the `k` the element.

```
Let's find out the 3rd largest number in the given array.

A = [19, 0, 34, 5, 6, 2, 85, 42]

---------

1. Select a pivot value randomly.

L = 0
R = len(A) - 1
pivot = A[(L + R) >> 1] = 5

2. Separate the array into two parts, smaller and bigger.

[0, 2] 5 [19, 34, 6, 85, 42]

3. Select the partition which `k-1`.
   Since we want to know the k-th largest,
   so `n - k - 1`.

[0, 2] 5 [19, 34, 6, 85, 42]
                  ↑


  A = [19, 34, 6, 85, 42]
-----

Then repeat from 1 again.

L = 0
R = 4
pivot = A[(0 + 4) >> 1] = 6 (again!)

[] 6 [19, 34, 85, 42]

Then choose one.

A = [19, 34, 85, 42]
-----

Then repeat from 1 again.

L = 0
R = 3
pivot = A[(0 + 3) >> 1] = 34

[19] 34 [85 42]

At this time, K - 1 (n - k - 1) does not exist in both partition.
Then we found 34.
```

In the above example, the original array is `[19, 0, 34, 5, 6, 2, 85, 42]`,
and `the 3rd largest element` is `34`.

```
0, 2, 5, 6, 19, 34, 42, 85
                ↑
```

### Time complexity

Remember the quick sort. The algorithm separates the given array into two parts.
This takes `O(log N)` times, and repeat each other `N` times. That's why `O(N log N)`.

```
A = [19, 0, 34, 5, 6, 2, 85, 42]
   ↓   ↓   ↓   ↓   ↓   ↓   ↓

quickSort([19, 0, 5, 6, 2])
quickSort([34, 85, 42])
```

But in the Quick Select, we just separate the array into two parts,
and one of the two partition does not do anything, then repeat this `N` times. That's why `O(N * log(N/2)) => O(N)`


# Reference

[How to find k-th smallest/largest element in an unsorted array?](https://medium.com/analytics-vidhya/how-to-find-k-th-smallest-largest-element-in-an-unsorted-array-4ab7015d802a)

[JavaScript implementation](https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/1405458/Javascript-QuickSelect)

[Compare QuickSort, HeapSort, and QuickSelect in python (and actually QuickSelect was slowest!)](https://leetcode.com/submissions/detail/574976004/)
