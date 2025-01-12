---
date created: 2025-01-11 21:39
date updated: 2025-01-11 21:41
tags:
  - Easy
---

Tags: [[Hash Table]], [[Linked List]], [[Two Pointers]]
Similar Questions: [[Linked List Cycle II]], [[Happy Number]]

## Question

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the`next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next`  pointer is connected to. **Note that `pos` is not passed as a parameter**.
Return `true`_ if there is a cycle in the linked list_. Otherwise, return `false`.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```java
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2:

![IMG](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```java
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3:

![IMG](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```java
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

### Constraints:

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Algorithm

### Set 
- Iterate over the list and add each node to a set
- If the node is already in the set return true 
### Hare & Tortoise algorithm
- Start 2 pointers fast and slow at the start of the list 
- The fast pointer will advance 2 nodes while the slow will only advance 1 node 


## Code

## Links

[LeetCode](https://leetcode.com/problems/linked-list-cycle/description/)
