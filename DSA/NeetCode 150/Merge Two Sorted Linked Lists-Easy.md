## Question
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.
### Example 1:



```java
Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]

```
### Example 2:


```java
Input: list1 = [], list2 = [1,2]

Output: [1,2]

```
### Example 3:


```java
Input: list1 = [], list2 = []

Output: []

```

Constraints:
0 <= The length of the each list <= 100.
-100 <= Node.val <= 100


### Recommended Time & Space Complexity

You should aim for a solution with O(n + m) time and O(1) space, where n is the length of list1 and m is the length of list2.

## Algorithm 
- Create a new list with a dummy start value
- Maintain a head and a tail (both will start as the same since there is only 1 element)
- While both list still have values 
	- Add the smaller one to the tail
- Once either one (or both) are empty we no longer need to compare values 
- Add all values from the list that is not empty to the result 
- Return the head.next to remove the dummy value we added in the beginning
## Code 
``` Java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2){
		
        ListNode dummy = new ListNode(0); // head

        ListNode node  = dummy; // tail 

        while (list1 != null && list2 != null){

            if (list1.val < list2.val){
                node.next = list1;
                list1 = list1.next;
            } else {
                node.next = list2;
                list2 = list2.next;
            }
            node = node.next;
        }

		// add all remaing elements from the either list to the result 
		// as all remaing elements are greater than what is in node 
        while (list1 != null){
            node.next = list1;
            list1 = list1.next;
            node = node.next;
        }

        while (list2 != null){
            node.next = list2;
            list2 = list2.next;
            node = node.next;
        }
        return dummy.next;
    }
}

```

## Links

[NeetCode](https://neetcode.io/problems/merge-two-sorted-linked-lists)

[LeetCode](https://leetcode.com/problems/merge-two-sorted-linked-lists)
