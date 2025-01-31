---
date created: 2025-01-30 23:54
date updated: 2025-01-30 23:55
tags:
  - Medium
---

Tags: [[Array]], [[Hash Table]], [[Greedy]], [[Sorting]], [[Heap (Priority Queue)]], [[Counting]]
Similar Questions: [[Rearrange String k Distance Apart]], [[Reorganize String]], [[Maximum Number of Weeks for Which You Can Work]], [[Find Minimum Time to Finish All Jobs II]], [[Task Scheduler II]]

## Question

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.
Return the **minimum** number of CPU intervals required to complete all tasks.

### Example 1:

```java

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

```

### Example 2:

```java

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

```

### Example 3:

```java

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

```

### Constraints:

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Algorithm
- There is a way to do this without a heap but I don't really understand it so were not doing it
- Count the occurrence of each task 
- Add the occurrence of each task to a max Heap 
- While there are still tasks in the heap 
	- Create a window of n + 1 unique tasks, in order of their occurrence
		- the first n elements of the max heap 
	- If we don't have enough tasks to complete the window add no-op idle tasks 
	- Decrement the occurrence of each task and add them back to the heap
- The total time is the number of windows minus any trailing idle tasks 
## Code

```java

class Solution {
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int[] counts = new int[26];

        for (char t : tasks)
            counts[t - 'A']++;

        for (int j : counts)
            if (j > 0)
                maxHeap.offer(j);

        int count = 0, trailing = 0;

        while (!maxHeap.isEmpty()) {
            count += trailing;
            trailing = 0;

            int[] temp = new int[n + 1]; // window 
            for (int i = 0; i < n + 1; i++) {
                int task = -1;
                if (!maxHeap.isEmpty()) {
                    task = maxHeap.poll(); // the element with the most occurences need to be started first 
                    task--;
                    count++;
                } else {
                    trailing++;
                }
                temp[i] = task;
            }
            for (int task : temp)
                if (task > 0)
                    maxHeap.offer(task);
        }
        return count;
    }
}


```

## Links

[LeetCode](https://leetcode.com/problems/task-scheduler/description/)
