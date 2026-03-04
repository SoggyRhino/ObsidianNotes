---
date created: 2025-01-22 19:16
tags:
  - Medium
---

Tags: [[Tree]], [[Breadth-First Search]], [[Binary Tree]]
Similar Questions: [[Binary Tree Zigzag Level Order Traversal]], [[Binary Tree Level Order Traversal II]], [[Minimum Depth of Binary Tree]], [[Binary Tree Vertical Order Traversal]], [[Average of Levels in Binary Tree]], [[N-ary Tree Level Order Traversal]], [[Cousins in Binary Tree]], [[Minimum Number of Operations to Sort a Binary Tree by Level]], [[Divide Nodes Into the Maximum Number of Groups]]

## Question

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

```java
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

### Example 2:

```java
Input: root = [1]
Output: [[1]]
```

### Example 3:

```java
Input: root = []
Output: []
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Algorithm
- Use any Tree Traversal Algorithm, keeping track of the current level
- Add each node to the list at the index of the current level 

## Code

## Links

[LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
