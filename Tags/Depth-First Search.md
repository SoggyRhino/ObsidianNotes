
## Code 

### Inorder Traversal of a binary Tree
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        
        while (current != null || !stack.isEmpty()) {
            // Traverse to the leftmost node, pushing all nodes along the way
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            
            // Process the current node
            current = stack.pop();
            result.add(current.val);
            
            // Move to the right subtree
            current = current.right;
        }
        
        return result;
    }
}
```