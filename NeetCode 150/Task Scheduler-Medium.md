## Question
You are given an array of CPU  tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
Return the minimum number of CPU cycles required to complete all tasks.
### Example 1:


```java
Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5

```
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.
### Example 2:


```java
Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9

```
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.
Constraints:
1 <= tasks.length <= 1000
0 <= n <= 100


### Recommended Time & Space Complexity

You should aim for a solution with O(m) time and O(1) space, where m is the size of the input array.






## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/task-scheduling)

[LeetCode](https://leetcode.com/problems/task-scheduling)
