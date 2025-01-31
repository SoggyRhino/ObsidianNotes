---
date created: 2025-01-30 23:35
tags:
  - Medium
date updated: 2025-01-30 23:52
---

Tags: [[Array]], [[Divide and Conquer]], [[Sorting]], [[Heap (Priority Queue)]], [[Quickselect]]
Similar Questions: [[Wiggle Sort II]], [[Top K Frequent Elements]], [[Third Maximum Number]], [[Kth Largest Element in a Stream]], [[K Closest Points to Origin]], [[Find the Kth Largest Integer in the Array]], [[Find Subsequence of Length K With the Largest Sum]], [[K Highest Ranked Items Within a Price Range]]

## Question

Given an integer array `nums` and an integer `k`, return _the_ `k^th` _largest element in the array_.
Note that it is the `k^th` largest element in the sorted order, not the `k^th` distinct element.
Can you solve it without sorting?

### Example 1:

```java
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2:

```java
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

### Constraints:

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Algorithm

### Heap

- For all in `nums`
- Add to Min-Heap
- If size of heap is > `k`
  - remove the smallest element `poll`

### Occurrence

- This is only efficient since we can only have numbers between -10000 and 10000
  - Otherwise we would use too much memory
- Create an occurrence array of size 200001
- For each in `nums`
  - Increase the value at the corresponding index
  - -10000 maps to index 0, 0 maps to index 10000, etc.
- Iterate over the occurrence back wards
  - Once we find an element that is > 0
    - Decrement the element
    - Decrement the `k`
  - If `k` is 0
    - Return the value that the current index corresponds to
  - If the value of the current index is 0
    - Go to the next index

## Code

### Heap

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        for (int num : nums){
            heap.offer(num);
            if (heap.size() > k)
                heap.poll();
        }

        return heap.poll();
    }
}
```

### Occurrence

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int[] count = new int[20001];

        for (int num : nums)
            count[num + 10000]++;

        for (int i =count.length-1; i >=0;){
            if (count[i] > 0 ){
                count[i]--;
                k--;        
            } else {
                i--;
            }

            if (k == 0)
                return i - 10000;
        }
        return 0;
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
