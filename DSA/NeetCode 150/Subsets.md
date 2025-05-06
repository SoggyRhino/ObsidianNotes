---
date created: 2025-02-07 21:36
tags:
  - Medium
---

Tags: [[Array]], [[Backtracking]], [[Bit Manipulation]]
Similar Questions: [[Subsets II]], [[Generalized Abbreviation]], [[Letter Case Permutation]], [[Find Array Given Subset Sums]], [[Count Number of Maximum Bitwise-OR Subsets]]

## Question

Given an integer array `nums` of **unique** elements, return _all possible_ subsets _(the power set)_.
The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Example 1:

```java
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### Example 2:

```java
Input: nums = [0]
Output: [[],[0]]
```

### Constraints:

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of

`nums` are **unique**.

## Algorithm

### Brute Force

- For each element in `nums`:
  - For each subset
    - Create a copy that has the current `num`
    - Create a copy that does not have the current `num`

### DFS

- Iterate over `nums` as a binary tree
  - For the left branch: include the current `num`
  - For the right branch: don't include it
  - Once we reach a leaf: save the current subset

## Code

### Brute Force

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        res.add(new ArrayList<>());

        for (int num : nums){
            int end = res.size();
            for (int i =0; i < end; i++){
                var list = new ArrayList(res.get(i));
                list.add(num);
                res.add(list);
            }
        }
        return res;
    }
}
```

### DFS

```java

public class Solution {
    
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        dfs(nums, 0, subset, res);
        return res;
    }

    private void dfs(int[] nums, int i, List<Integer> subset, List<List<Integer>> res) {
        if (i >= nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }
        subset.add(nums[i]);
        dfs(nums, i + 1, subset, res);
        subset.remove(subset.size() - 1);
        dfs(nums, i + 1, subset, res);
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/subsets/description/)
