---
date created: 2025-01-25 15:54
date updated: 2025-01-25 15:56
tags:
  - Medium
---

Tags: [[Tree]], [[Depth-First Search]], [[Breadth-First Search]], [[Binary Tree]]
Similar Questions: [[Populating Next Right Pointers in Each Node]], [[Boundary of Binary Tree]]

## Question

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return _the values of the nodes you can see ordered from top to bottom_.

### Example 1:

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

```java
Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]
```

### Example 2:

![](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

```java
Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]
```

**Example 3:**

```java
Input: root = [1,null,3]

Output: [1,3]
```

**Example 4:**

```java
Input: root = []

Output: []
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Algorithm
- Preform Breath first search of the tree
- For each level add children from left to right 
- The last child per level is the rightest and is added  to the list 

## Code
```java

class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> list = new ArrayList<>(); // we always return a list so initalize before guard
        if (root == null)
            return list;

        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);

        while (!queue.isEmpty()) {
		    //we might increase the size of queue so we keep track of the number on this level
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                var current = queue.poll();

                if (current.left != null)  //add left to right 
                    queue.add(current.left);
                if (current.right != null) 
                    queue.add(current.right);
                    
                if (i == size -1) //last value on the level is the furthest right 
                    list.add(current.val);
            }
        }
        
        return list;
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/description/)
