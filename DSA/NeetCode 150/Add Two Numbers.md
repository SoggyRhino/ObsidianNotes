---
date created: 2025-01-17 22:23
tags:
  - Medium
---

Tags: [[Linked List]], [[Math]], [[Recursion]]
Similar Questions: [[Multiply Strings]], [[Add Binary]], [[Sum of Two Integers]], [[Add Strings]], [[Add Two Numbers II]], [[Add to Array-Form of Integer]], [[Add Two Polynomials Represented as Linked Lists]], [[Double a Number Represented as a Linked List]]

## Question

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum
as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1:

![IMG](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```java
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2:

```java
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3:

```java
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

### Constraints:

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Algorithm
- Create



## Code

```Java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0, null);
        ListNode node = dummy;

        int carry = 0;
        while (l2 != null || l1 != null) {
            int x = 0, y = 0;

            if (l1 != null) {
                x = l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                y = l2.val;
                l2 = l2.next;
            }
            carry = x + y + carry > 9 ? 1 : 0;
            node.next = new ListNode(x + y + carry - (carry * 10) , null);
            node = node.next;
        }

        if (carry > 0)
            node.next = new ListNode(1, null);

        return dummy.next;
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/add-two-numbers/description/)
