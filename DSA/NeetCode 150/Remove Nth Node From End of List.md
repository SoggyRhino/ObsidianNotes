---
date created: 2025-01-17 21:25
tags:
  - Medium
---

Tags: [[Linked List]], [[Two Pointers]]
Similar Questions: [[Swapping Nodes in a Linked List]], [[Delete N Nodes After M Nodes of a Linked List]], [[Delete the Middle Node of a Linked List]]

## Question

Given the `head` of a linked list, remove the `n^th` node from the end of the list and return its head.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```java
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:

```java
Input: head = [1], n = 1
Output: []
```

### Example 3:

```java
Input: head = [1,2], n = 1
Output: [1]
```

### Constraints:

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

## Algorithm
- Start a left pointer at index -1 and a right pointer at index 0;
- Advance the right pointer n spaces
	- Now the left.next will be the current nth from the end (we need the nth's parent to delete it)
- While the right has not reached the end, advance both pointers 
- Remove the nth node (left's child)
	- `left.next = left.next.next'
- Return the original head



## Code

```Java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode left = dummy;
        ListNode right = head;
        while (n-- > 0)
            right = right.next;

        while (right != null){
            left = left.next;
            right = right.next;
        }

        left.next = left.next.next;
        return dummy.next;
    }
}

```

## Links

[LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
[NeetCode](https://neetcode.io/problems/remove-node-from-end-of-linked-list)