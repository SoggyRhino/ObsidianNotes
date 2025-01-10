---
date created: 2025-01-09 15:38
date updated: 2025-01-09 21:02
tags:
  - Medium
---

Tags: [[Array]], [[Two Pointers]], [[Sorting]]
Similar Questions: [[Two Sum]], [[3Sum Closest]], [[4Sum]], [[3Sum Smaller]], [[Number of Arithmetic Triplets]], [[Minimum Sum of Mountain Triplets I]], [[Minimum Sum of Mountain Triplets II]]

## Question

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

### Example 1:

```java
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

### Example 2:

```java
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Example 3:

```java
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

### Constraints:

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Algorithm

- Sort the Array
- Iterate over the list excluding the last 2 places (we need 3 values to find a solution)
  - If the value at the current index is the same as the last index skip
    - This will ensure that we don't get duplicate solutions
  - Create a pointer `left` at the current index and a pointer `right` at the end of the array
  - While `left < right`
  - Check if they sum to 0
    - If they do, add the values to the list and move `left` and `right` inward
      - `left++` `right--`
    - If the sum is greater than 0 then decrease `right` by 1
    - If the sum is less than 0 then increase `left` by 1
- Return the list

## Code

```java
class Solution {

    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> results = new ArrayList<>();

        Arrays.sort(nums);

  

        for (int i = 0; i < nums.length - 2; i++) {

            if (i > 0 && nums[i] == nums[i - 1])

                continue;

  

            int left = i + 1;

            int right = nums.length - 1;

  

            while (left < right) {

                int sum = nums[i] + nums[left] + nums[right];

                if (sum > 0) {

                    right--;

                } else if (sum < 0) {

                    left++;

                } else {
                    results.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;

                    // keep shifting right until num[left] is different from before

                    while (left < right && nums[left] == nums[left - 1])

                        left++;

                }

            }
        }
        return results;

    }

}
```

## Links

[NeetCode](https://neetcode.io/problems/three-integer-sum)

[LeetCode](https://leetcode.com/problems/3sum/)
