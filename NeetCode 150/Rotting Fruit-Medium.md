## Question
You are given a 2-D matrix grid. Each cell can have one of three possible values:
0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.
Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.
### Example 1:



```java
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4

```
### Example 2:


```java
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1

```
Constraints:
1 <= grid.length, grid[i].length <= 10


### Recommended Time & Space Complexity

You should aim for a solution with O(m * n) time and O(m * n) space, where m is the number of rows and n is the number of columns in the given grid.





## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/rotting-fruit)

[LeetCode](https://leetcode.com/problems/rotting-fruit)
