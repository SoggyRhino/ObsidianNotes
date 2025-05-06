---
date created: 2025-02-09 21:36
tags:
  - Medium
date updated: 2025-02-09 21:39
---

Tags: [[Array]], [[Backtracking]]
Similar Questions: [[Next Permutation]], [[Permutations II]], [[Permutation Sequence]], [[Combinations]]

## Question

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

### Example 1:

```java
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2:

```java
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3:

```java
Input: nums = [1]
Output: [[1]]
```

### Constraints:

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Algorithm

### Iteration
- We start with a list of all the subsets we have already created
	- Empty at the beginning 
- For each `num` in `nums`
	- For each subset 
		- Create a copy where `num` is inserted at each index 
		- Add the copies to the list of found subsets 
### Backtracking

- Base Case : the permutation has all the elements of `nums`
- Recursive step: 
	- For all `num` in `nums`
		- If the current permutation doesn't contain `num`, add it to the end 
		- Then recursively call the function to generate all the permutations that start with the current permutation 
		- Then we backtrack and remove `num` so that we can try other values in `nums` at the current index 

## Code

### Iteration

```java
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> perms = new ArrayList<>();
        perms.add(new ArrayList<>());

        for (int num : nums) {
            List<List<Integer>> new_perms = new ArrayList<>();
            for (List<Integer> p : perms) {
                for (int i = 0; i <= p.size(); i++) {
                    List<Integer> p_copy = new ArrayList<>(p);
                    p_copy.add(i, num);
                    new_perms.add(p_copy);
                }
            }
            perms = new_perms;
        }
        return perms;
    }
}
```

### Backtracking

```java

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        boolean[] used =  new boolean[nums.length];
        helper(nums, used, new ArrayList<>(), res);
        return res;
    }


    public void helper(int[] nums, boolean[] used, List<Integer> current, List<List<Integer>> res ){
        if (current.size() == nums.length){
            res.add(new ArrayList<>(current));
            return;
        }

        for (int i =0; i < nums.length; i++){
            if (!used[i]){
                current.add(nums[i]);// lock in nums[i] for this position 
                used[i] = true;
                helper(nums,used,current,res); //generate all permutations that start with current
                current.removeLast(); // this is the backtrack, try all other values for the current index
                used[i] = false;
            }
        }
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/permutations/description/)
