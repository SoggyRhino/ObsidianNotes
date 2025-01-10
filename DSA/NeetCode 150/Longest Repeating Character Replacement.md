---
date created: 2025-01-10 13:56
tags:
  - Medium
date updated: 2025-01-10 14:28
---

Tags: [[Hash Table]], [[String]], [[Sliding Window]]
Similar Questions: [[Longest Substring with At Most K Distinct Characters]], [[Max Consecutive Ones III]], [[Minimum Number of Operations to Make Array Continuous]], [[Maximize the Confusion of an Exam]], [[Longest Substring of One Repeating Character]]

## Question

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

### Example 1:

```java
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### Example 2:

```java
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

### Constraints:

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Algorithm

- Start a `left` pointer a 0
- Iterate over each index of the string `s` with pointer `right`
  - Update the Max Frequency
  - If the new substring  (left to right) is not valid `(right - left + 1) - MaxFrequency > k`
    - Move the left pointer to the right until it is valid
    - Update count
  - Update result
  
- 

## Code

```java

public class Solution {

    public int characterReplacement(String s, int k) {

        HashMap<Character, Integer> count = new HashMap<>();
        int res = 0;
        int l = 0, maxf = 0;

        for (int r = 0; r < s.length(); r++) {
            count.put(s.charAt(r), count.getOrDefault(s.charAt(r), 0) + 1);
            maxf = Math.max(maxf, count.get(s.charAt(r)));
  
            while ((r - l + 1) - maxf > k) {
                count.put(s.charAt(l), count.get(s.charAt(l)) - 1);
                l++;
            }

            res = Math.max(res, r - l + 1);
        }
        return res;

    }

}
```

## Links

[LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/description/)
