---
date created: 2025-01-20 21:02
tags:
  - Easy
---

Tags: [[Tree]], [[Depth-First Search]], [[Binary Tree]]
Similar Questions: [[Maximum Depth of Binary Tree]], [[K-th Largest Perfect Subtree Size in Binary Tree]], [[Check Balanced String]]

## Question

Given a binary tree, determine if it is height-balanced.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```java
Input: root = [3,9,20,null,null,15,7]
Output: true
```

### Example 2:

![IMG](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```java
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

### Example 3:

```java
Input: root = []
Output: true
```

### Constraints:

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Algorithm

- DFS the tree keeping track of the height of each node 
	- If the heights of the left and right subtrees differ by more than 1 return false
	- Else update the current height to `max(leftHeight, rightheight) + 1`

- There is a better implementation but it is too confusing, maybe come back after more dfs

## Code

```java

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;

        HashMap<TreeNode, Integer> visited = new HashMap<>();
        visited.put(null, 0);
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while(!stack.isEmpty()){
            TreeNode current = stack.peek();

            if (current.left != null && !visited.containsKey(current.left)){
                stack.push(current.left);
            } else if (current.right != null && !visited.containsKey(current.right)){
                stack.push(current.right);
            } else {
                current = stack.pop();
                int left = visited.get(current.left), right = visited.get(current.right);
                if (Math.abs(left - right) > 1)
                    return false;
                visited.put(current, 1 + Math.max(left,right));
            }
        }
        return true;
    }
}




```

## Links

[LeetCode](https://leetcode.com/problems/balanced-binary-tree/description/)
