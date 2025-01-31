---
date created: 2025-01-30 23:35
tags:
  - Medium
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
	- Other wise we would use too much memory 
- Create an array of size 200001 
	- -10000 maps to 0, 0 maps to 10000, etc 
	- 
 - For each in `nums`
	 - Increase the value at the index in the 



## Code

## Links

[LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
