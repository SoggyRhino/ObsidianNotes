---
date created: 2025-01-17 23:25
tags:
  - Easy
---

Tags: [[Tree]], [[Depth-First Search]], [[Breadth-First Search]], [[Binary Tree]]
Similar Questions: [[Balanced Binary Tree]], [[Minimum Depth of Binary Tree]], [[Maximum Depth of N-ary Tree]], [[Time Needed to Inform All Employees]], [[Amount of Time for Binary Tree to Be Infected]], [[Height of Binary Tree After Subtree Removal Queries]]

## Question

Given the `root` of a binary tree, return _its maximum depth_.
A binary tree's **maximum depth**
is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```java
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Example 2:

```java
Input: root = [1,null,2]
Output: 2
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Algorithm
- Recursively traverse the tree, keeping track of the current depth
- If the current node is null, return the current depth
- Else return the max of the depth of the left and right nodes

## Code

```
class Solution {
    public int maxDepth(TreeNode root) {
        return rec(root,0);
    }

    public int rec(TreeNode node, int n){
        if (node == null)
            return n;
        return Math.max(rec(node.left, n+1), rec(node.right, n+1));


    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

[NeetCode](https://neetcode.io/problems/depth-of-binary-tree)
