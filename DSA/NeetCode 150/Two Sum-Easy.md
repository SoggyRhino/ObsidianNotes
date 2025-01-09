---
date created: 2025-01-09 15:59
date updated: 2025-01-09 16:00
---

## Question

Given an array of integers `nums` and an integer target, return the indices `i` and j such that `nums[i] + nums[j] == target` and`  i != j `.
You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.
Return the answer with the smaller index first.

### Example 1:

```java
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

```

Explanation: `nums[0] + nums[1] == 7`, so we return `[0, 1]`.

### Example 2:

```java
Input: nums = [4,5,6], target = 10

Output: [0,2]

```

### Example 3:

```java
Input: nums = [5,5], target = 10

Output: [0,1]

```

Constraints:
`2 <= nums.length <= 1000`
`-10,000,000 <= nums[i] <= 10,000,000`
`-10,000,000 <= target <= 10,000,000`

### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

## Algorithm
- 

## Code

```java 
class Solution {

    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int current = nums[i];

            if (map.containsKey(target - current))

                return new int[] { map.get(target - current), i };

            else

                map.put(current, i);

        }

        return new int[] { -1, -1 };

    }

}
```

```C++
class Solution {

public:

        std::vector<int> twoSum(std::vector<int>& nums, int target) {

        std::unordered_map<int,int> map;

        for (int i =0; i < nums.size(); i++){

            int comp = target - nums[i];

            if (map.find(comp) != map.end())

                return {i, map[comp]};

            map[nums.at(i)] = i;

        }

        return {};

    }

};

```
## Links

[NeetCode](https://neetcode.io/problems/two-integer-sum)

[LeetCode](https://leetcode.com/problems/two-sum/)
