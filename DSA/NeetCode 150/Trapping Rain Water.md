---
date created: 2025-01-09 21:08
tags:
  - Hard
date updated: 2025-01-09 21:09
---

Tags: [[Array]], [[Two Pointers]], [[Dynamic Programming]], [[Stack]], [[Monotonic Stack]]
Similar Questions: [[Container With Most Water]], [[Product of Array Except Self]], [[Trapping Rain Water II]], [[Pour Water]], [[Maximum Value of an Ordered Triplet II]]

## Question

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```java
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2:

```java
Input: height = [4,2,0,3,2,5]
Output: 9
```

### Constraints:

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Algorithm

- Create left and right pointer at 0 and `heights.length -1` respectively 
- While left is less than right 
	- Find the current Area, `min(heights[left],heights[right]) * right - left`
	- Move the pointer with the smaller point inward 
		- `left++` or `right--`


## Code

```java

class Solution {
    public int trap(int[] height) {
        int right = height.length - 1;
        int water = 0;
        int left = 0;

        while (left < right) {

            int level = Math.max(level, Math.min(height[left], height[right]));

            if (height[left] < height[right]) {
                water += Math.max(0, level - height[left]);
                left++;

            } else {
                water += Math.max(0, level - height[right]);
                right--;

            }
        }
        return water;

    }

}
```

## Links

[LeetCode](https://leetcode.com/problems/trapping-rain-water/description/)
