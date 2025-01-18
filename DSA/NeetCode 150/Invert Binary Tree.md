---
date created: 2025-01-17 23:21
tags:
  - Easy
---

Tags: [[Tree]], [[Depth-First Search]], [[Breadth-First Search]], [[Binary Tree]]
Similar Questions: [[Reverse Odd Levels of Binary Tree]]

## Question

Given the `root` of a binary tree, invert the tree, and return _its root_.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```java
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

### Example 2:

![IMG](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```java
Input: root = [2,1,3]
Output: [2,3,1]
```

### Example 3:

```java
Input: root = []
Output: []
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Algorithm
- While the current node is not null, swap the left and right nodes
- Repeat recursively for the left node and the right node
	- (swap each node's children)

## Code

```
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null){
            return null;
        }

        var temp = root.right;
        root.right = root.left;
        root.left = temp;

        invertTree(root.right);            
        invertTree(root.left);

        return root;
    }
}

```

## Links

[LeetCode](https://leetcode.com/problems/invert-binary-tree/description/)
[NeetCode](https://neetcode.io/problems/invert-a-binary-tree)