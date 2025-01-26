## Code 

### Iterative 

```java

public void rightSideView(TreeNode root) {
    Queue<TreeNode> queue = new ArrayDeque<>();
    if (root != null)
        queue.add(root);
        
    while (!queue.isEmpty()) {
        int size = queue.size(); //keep track of the last node of the current level since we adding new nodes to the queue 
        for (int i = 0; i < size; i++) { // add all the nodes of the next level to the queue 
            var current = queue.poll();
            //do something here 
            if (current.left != null) 
                queue.add(current.left);
            if (current.right != null) 
                queue.add(current.right);
        }
    }
}
```
