---
date created: 2025-01-22 18:36
tags:
  - Easy
date updated: 2025-01-22 18:36
---

Tags: [[Tree]], [[Depth-First Search]], [[Breadth-First Search]], [[Binary Tree]]
Similar Questions:

## Question

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```java
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

### Example 2:

![IMG](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```java
Input: p = [1,2], q = [1,null,2]
Output: false
```

### Example 3:

![IMG](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```java
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

### Constraints:

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Algorithm
- Just use any traversal algorithm with both lists at the same time 

## Code

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null){
            return true;
        }
        if(p==null || q==null){
            return false;
        }
        if(p.val!=q.val){
            return false;
        }
        return isSameTree(p.left,q.left)&& isSameTree(p.right,q.right);
    }
}

```

## Links

[LeetCode](https://leetcode.com/problems/same-tree/description/)
