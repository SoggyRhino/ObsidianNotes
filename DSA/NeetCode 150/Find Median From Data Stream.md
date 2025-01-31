---
date created: 2025-01-31 00:04
tags:
  - Hard
---

Tags: [[Two Pointers]], [[Design]], [[Sorting]], [[Heap (Priority Queue)]], [[Data Stream]]
Similar Questions: [[Sliding Window Median]], [[Finding MK Average]], [[Sequentially Ordinal Rank Tracker]], [[Minimum Operations to Make Median of Array Equal to K]], [[Minimum Operations to Make Subarray Elements Equal]]

## Question

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the Median Finder class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

### Example 1:

```java
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Constraints:

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

**Follow up:**

- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Algorithm


### Overview 
 - We split the stream into a left and right side 
	 - Left is all the values less than the mean, and is a Max-Heap 
		 - This is because we only care about the greatest value on the left side (closest to the middle)
	- Right is all the values greater than the mean, and is a Min-Heap 
		 - This is because we only care about the least value on the left side (closest to the middle)

### Adding a Number 

- We add to the right side if the number is greater than the smallest number on the right 
	- `num > right.peek()`
- Otherwise we add it to the left side 
- If the right side has more than 1 more element than the left 
	- Remove the smallest element from the right and add it to the left 
- If the left side has more than 1 more element than the right 
	- Remove the largest element from the left and add it to the right 

### Finding the Median
- If each side has an equal number of values 
	- Return the average of the 2 middle values 
- Otherwise return the value from the side with the most elements 
	- This is the left side in the following implementation
## Code

```java 
class MedianFinder {
    PriorityQueue<Integer> left;
    PriorityQueue<Integer> right;


    public MedianFinder() {
        this.left = new PriorityQueue<>(Collections.reverseOrder());
        this.right = new PriorityQueue<>();
    }

    public void addNum(int num) {
        if (!right.isEmpty() && num > right.peek()) {
            right.offer(num);
            if (right.size() > left.size())
                left.offer(right.poll());
        } else {
            left.offer(num);
            if (left.size() - right.size() > 1)
                right.offer(left.poll());
        }
    }

    public double findMedian() {
        if ((left.size() + right.size())  % 2 == 0)
            return (left.peek() + right.peek()) / 2.0;
        return left.peek();
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/find-median-from-data-stream/description/)
