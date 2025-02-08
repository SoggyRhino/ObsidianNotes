---
date created: 2025-02-07 21:36
tags:
  - Medium
date updated: 2025-02-07 21:41
---

Tags: [[Array]], [[Backtracking]]
Similar Questions: [[Letter Combinations of a Phone Number]], [[Combination Sum II]], [[Combinations]], [[Combination Sum III]], [[Factor Combinations]], [[Combination Sum IV]], [[The Number of Ways to Make the Sum]]

## Question

Given an array of **distinct** integers `candidates` and a target integer `target`, return _a list of all **unique combinations** of _`candidates`_ where the chosen numbers sum to _`target`_._ You may return the combinations in **any order**.
The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

### Example 1:

```java
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

### Example 2:

```java
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

### Example 3:

```java
Input: candidates = [2], target = 1
Output: []
```

### Constraints:

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

## Algorithm

- Essentially the same as [[Subsets]] where we treat `canidates` as a tree
- For each `canidates[i]` we:
  - Include it in the current set and go the the next value
  - Include it in the current set and allow it to be reused
  - Exclude the value and go the the next distinct value
    - The array is already distinct so its just the next value
  - Break early if target is exceeded (only positive numbers are allowed)

## Code

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();

        dfs(nums,target, 0, 0, new ArrayList<>(), res);
        return res;
    }

    public void dfs(int[] nums, int target, int i, int sum, List<Integer> cur, List<List<Integer>> res){
        if (sum > target || i == nums.length){
            return;
        } if (sum == target) { 
            res.add(new ArrayList<>(cur));
            return;
        }
 
        cur.add(nums[i]);
        dfs(nums,target, i, sum + nums[i], cur, res);  //branch that continues to use the the current num 

        cur.remove(cur.size()-1);
        dfs(nums,target, i + 1, sum, cur, res);       //branch that does not contain any more of the current num
    }
}
```

## Links
[LeetCode](https://leetcode.com/problems/combination-sum/)