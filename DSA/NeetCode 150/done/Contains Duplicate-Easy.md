---
date created: 2025-01-09 15:57
date updated: 2025-01-09 17:11
---

Tags: [[Hash Table]]
Similar Questions: [[Contains Duplicate II-Easy]], [[Contains Duplicate III-Hard]], [[Make Array Zero by Subtracting Equal Amounts-Easy]]
## Question

Given an integer array `nums`, return true if any value appears more than once in the array, otherwise return false.

### Example 1:

```java
Input: nums = [1, 2, 3, 3]

Output: true

```

### Example 2:

```java
Input: nums = [1, 2, 3, 4]

Output: false

```

### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

## Algorithm

- Make a Set
- for each element
  -If set contains element return true
- Otherwise return false

## Code

```java
public class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
```

## Links

[NeetCode](https://neetcode.io/problems/duplicate-integer)

[LeetCode](https://leetcode.com/problems/contains-duplicate)


