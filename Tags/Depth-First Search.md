
## Code 

### In-Order Traversal of a binary Tree
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        
        while (current != null || !stack.isEmpty()) {
            // Go all the way down the rigth side (until there is a null)
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            
            // Process the current node (furthest left node)
            current = stack.pop();
            result.add(current.val);
            
            // Move to the right subtree
            // We can ignore null since it will become the next in the stack on line 15
            current = current.right;
        }
        
        return result;
    }
}
```