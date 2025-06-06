---
date created: 2025-01-09 20:22
date updated: 2025-01-09 21:00
tags:
  - Medium
---

Tags: [[Array]], [[Two Pointers]], [[Greedy]]
Similar Questions: [[Trapping Rain Water]], [[Maximum Tastiness of Candy Basket]], [[House Robber IV]]

## Question

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i^th` line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return _the maximum amount of water a container can store_.
**Notice** that you may not slant the container.

### Example 1:

![IMG](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```java
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2:

```java
Input: height = [1,1]
Output: 1
```

### Constraints:

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Algorithm

- Create left and right pointer at 0 and `heights.length -1` respectively 
- While left is less than right 
	- Find the current Area, `min(heights[left],heights[right]) * right - left`
	- Update the Max 
	- Move the pointer with the smaller point inward 
		- `left++` or `right--`

## Code

```java 

class Solution {

    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length-1;
        int max =0;
        
        while (left < right){
            int current = (right - left) * Math.min(heights[left], heights[right]);
            max = Math.max(max,current);

            if (heights[left] < heights[right]){
                left++;
            } else {
                right--;
            }
        }
        return max;
    }

}
```

## Links

[LeetCode](https://leetcode.com/problems/container-with-most-water/description/)
[NeetCode](https://neetcode.io/problems/max-water-container)