---
date created: 2025-01-30 23:18
tags:
  - Medium
---

Tags: [[Array]], [[Math]], [[Divide and Conquer]], [[Geometry]], [[Sorting]], [[Heap (Priority Queue)]], [[Quickselect]]
Similar Questions: [[Kth Largest Element in an Array]], [[Top K Frequent Elements]], [[Top K Frequent Words]], [[Find Nearest Point That Has the Same X or Y Coordinate]], [[Minimum Rectangles to Cover Points]], [[K-th Nearest Obstacle Queries]]

## Question

Given an array of `points` where `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.
The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `√(x<sub>1</sub> - x<sub>2</sub>)^2 + (y<sub>1</sub> - y<sub>2</sub>)^2`).
You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

```java
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

### Example 2:

```java
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

### Constraints:

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4`

## Algorithm

## Code

## Links

[LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/description/)
