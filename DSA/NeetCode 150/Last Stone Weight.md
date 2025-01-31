---
date created: 2025-01-30 23:12
tags:
  - Easy
---

Tags: [[Array]], [[Heap (Priority Queue)]]
Similar Questions:

## Question

You are given an array of integers `stones` where `stones[i]` is the weight of the `i^th` stone.
We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.
Return _the weight of the last remaining stone_. If there are no stones left, return `0`.

### Example 1:

```java
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
```

### Example 2:

```java
Input: stones = [1]
Output: 1
```

### Constraints:

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Algorithm
- Add all elements to a max Heap (reversed min heap/ priority queue)
- While there is at least 2 elements in the heap 
	- Remove the top 2 elements (2 largest still existing)
	- If they are equal discard both rocks 
	- Else add the resulting rock back to the heap 
		- `first - second`
- Return the remaining element in the heap or 0 if it does not exist


## Code

```java 
class Solution {
    public int lastStoneWeight(int[] stones) {
        int n = stones.length;

        while ( n > 1){
            Arrays.sort(stones);
            int x = stones[n-1];
            int y = stones[n-2];

            if ( x == y){
                n -=2;
            } else {
                stones[n-2] = x-y;
                n -=1;
            }
        }
        return n == 0 ? 0 : stones[0];
    }
}
```

## Links

[LeetCode](https://leetcode.com/problems/last-stone-weight/description/)
