---
date created: 2025-01-09 17:50
---
Tags: [[Array]] [[Two Pointers]] [[Greedy]]
Similar Questions: 
## Question

You are given an integer array `heights` where `heights[i]` represents the height of the 'ith' bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

### Example 1:

```java
Input: height = [1,7,2,5,4,7,3,6]

Output: 36

```

### Example 2:

```java
Input: height = [2,2,2]

Output: 4

```

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000

### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

## Algorithm

## Code

```java
class Solution {

    public int maxArea(int[] height) {

        int left = 0;

        int right = height.length-1;

  

        int max =0;

  
  

        while (left < right){

            int h1 = height[left];

            int h2 = height[right];

            max = Math.max(max,(right - left) * Math.min(h1, h2));

  

            if (h1 < h2){

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

[NeetCode](https://neetcode.io/problems/max-water-container)

[LeetCode](https://leetcode.com/problems/max-water-container)
