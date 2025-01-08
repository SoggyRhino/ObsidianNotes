## Question
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.
### Example 1:



```java
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6

```
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.
Constraints:
1 <= grid.length, grid[i].length <= 50


### Recommended Time & Space Complexity

You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the grid.





## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/max-area-of-island)

[LeetCode](https://leetcode.com/problems/max-area-of-island)
