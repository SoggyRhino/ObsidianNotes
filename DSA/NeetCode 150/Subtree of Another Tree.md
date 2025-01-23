---
date created: 2025-01-22 18:42
tags:
  - Easy
---

Tags: [[Tree]], [[Depth-First Search]], [[String Matching]], [[Binary Tree]], [[Hash Function]]
Similar Questions: [[Count Univalue Subtrees]], [[Most Frequent Subtree Sum]]

## Question

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of`  subRoot ` and `false` otherwise.
A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

```java
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

### Example 2:

![IMG](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

```java
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

### Constraints:

- The number of nodes in the `root` tree is in the range `[1, 2000]`.
- The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Algorithm
- See if every sub tree is equal to the provided using  [[Same Tree]]'s Algorithm

## Code

```java 
class Solution {  

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {

        if (subRoot == null) {

            return true;

        }

        if (root == null) {

            return false;

        }

  

        if (isSameTree(root,subRoot))

            return true;

  

        return isSubtree(root.left,subRoot) || isSubtree(root.right,subRoot);

    }

  

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

[LeetCode](https://leetcode.com/problems/subtree-of-another-tree/description/)
