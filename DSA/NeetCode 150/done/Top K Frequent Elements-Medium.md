---
date created: 2025-01-07 18:58
date updated: 2025-01-09 16:16
tags:
---

Tags: [[Hash Table]], [[Array]], [[Heap]]
Similar Questions: [[Word Frequency-Medium]], [[Kth Largest Element in an Array-Medium]], [[Sort Characters By Frequency-Medium]], [[Split Array into Consecutive Subsequences-Medium]], [[Top K Frequent Words-Medium]], [[K Closest Points to Origin-Medium]], [[Sender With Largest Word Count-Medium]], [[Most Frequent Even Element-Easy]]

## Question

Given an integer array `nums` and an integer `k`, return the  `k` most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

### Example 1:

```java
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

```

### Example 2:

```java
Input: nums = [7,7], k = 1

Output: [7]

```

### Constraints:

`1 <= nums.length <= 10^4.`
`-1000 <= nums[i] <= 1000`
`  1 <= k <= number of distinct elements in nums. `

### Recommended Time & Space Complexity

You should aim for a solution with `O(n)` time and `O(n)` space, where n is the size of the input array.

## Algorithm
- Use a HashMap to store the count of each element in the array 
- Create a Heap (Priority Queue) 
	- Sort by second value in a pair 
- Add each pair (value and count) to the heap
- Pop the k elements from the list and return as an array

## Code

```java 

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // O(1) time
        if (k == nums.length) {
            return nums;
        }
        
        // 1. Build hash map: character and how often it appears
        // O(N) time
        Map<Integer, Integer> count = new HashMap();
        for (int n: nums) {
          count.put(n, count.getOrDefault(n, 0) + 1);
        }

        // init heap 'the less frequent element first'
        Queue<Integer> heap = new PriorityQueue<>(
            (n1, n2) -> count.get(n1) - count.get(n2));

        // 2. Keep k top frequent elements in the heap
        // O(N log k) < O(N log N) time
        for (int n: count.keySet()) {
          heap.add(n);
          if (heap.size() > k) heap.poll();    
        }

        // 3. Build an output array
        // O(k log k) time
        int[] top = new int[k];
        for(int i = k - 1; i >= 0; --i) {
            top[i] = heap.poll();
        }
        return top;
    }
}
```

```C++
  

#include <vector>

#include <unordered_map>

#include <algorithm>  

  
  

class Solution {

public:

    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {

        std::unordered_map<int,int> map;

        for (int num : nums)

            map[num]++;

  

        std::vector<std::pair<int, int>> arr;

        for (const auto& p : map) {

            arr.push_back({p.second, p.first});

        }

        std::sort(arr.rbegin(), arr.rend());

  

        std::vector<int> result;

        result.reserve(k);

        for (int i =0; i < k; i++)

            result.push_back(arr[i].second);

        return result;

    }

};
```

## Links

[NeetCode](https://neetcode.io/problems/top-k-elements-in-list)

[LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
