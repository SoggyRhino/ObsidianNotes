Tags: [[Array]], [[Backtracking]], [[Bit Manipulation]]
Similar Questions: [[Subsets]], [[Find Array Given Subset Sums]]
## Question

Given an integer array `nums` that may contain duplicates, return _all possible_ subsets_ (the power set)_.
The solution set **must not** contain duplicate subsets. Return the solution in **any order**.


### Example 1:

```java
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2:

```java
Input: nums = [0]
Output: [[],[0]]
```



### Constraints:

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Algorithm
- Essentially the same as  [[Combination Sum]], just without the constraint of needing to sum to a number 
- We take care of duplicate subsets by sorting the array 
- For each index in `nums`
	- Create a subset that includes the value `nums` at that index 
		- Move on to the next index
	- Create a subset that does not include the value `nums` at that index 
		- Skip indexes until the value at `nums` is a different number 
			- This creates a new branch contains no more of the current value at `nums`


## Code

```java 

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        helper(nums, 0 , new ArrayList<>(), res);
        return res;
        
    }

    public void helper(int[] nums, int i, List<Integer> cur, List<List<Integer>> res){
        if (i == nums.length){
            res.add(new ArrayList<>(cur));
            return;
        }

        int num = nums[i];

        cur.add(num);
        helper(nums, i + 1, cur, res);
        cur.removeLast();

        while (i < nums.length && nums[i] == num)
            i++;

        helper(nums, i, cur, res);

    }
}
```

## Links
[LeetCode](https://leetcode.com/problems/subsets-ii/)