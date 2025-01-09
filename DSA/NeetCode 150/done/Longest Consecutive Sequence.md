---
date created: 2025-01-09 17:15
date updated: 2025-01-09 17:17
tags:
  - Medium
---

Tags: [[Array]], [[Hash Table]]
Similar Questions: [[Find Three Consecutive Integers That Sum to a Given Number]], [[Maximum Consecutive Floors Without Special Floors]], [[Length of the Longest Alphabetical Continuous Substring]], [[Find the Maximum Number of Elements in Subset]]

## Question

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

### Example 1:

```java
Input: nums = [2,20,4,10,3,4,5]

Output: 4

```

Explanation: The longest consecutive sequence is `[2, 3, 4, 5]`.

### Example 2:

```java
Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

```

Constraints:
`0 <= nums.length <= 1000`
`-10^9 <= nums[i] <= 10^9`

### Recommended Time & Space Complexity

You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

## Algorithm
- Create a set of all elements in `nums`
- For each element in `nums` 
	-  while the element + 1 exists in the set 
		- increase the length 
	- Updated the max length
- Return the max length

## Code

```java

class Solution {

    public int longestConsecutive(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for (int i : nums){

            set.add(i);

        }

  

        int longest = 0;

        for (int i : set){

            //if i is the start of a sequence

            if (!set.contains(i-1)){

                int temp = i;

  

                while (set.contains(temp)){

                    temp++;

                }

  

                longest = Math.max(longest, temp -i);

            }

        }

  

        return longest;

  

    }

}
```

## Links

[NeetCode](https://neetcode.io/problems/longest-consecutive-sequence)

[LeetCode](https://leetcode.com/problems/longest-consecutive-sequence)
