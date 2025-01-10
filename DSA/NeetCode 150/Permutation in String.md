---
date created: 2025-01-10 14:36
date updated: 2025-01-10 15:02
tags:
  - Medium
---

Tags: [[Hash Table]], [[Two Pointers]], [[String]], [[Sliding Window]]
Similar Questions: [[Minimum Window Substring]], [[Find All Anagrams in a String]]

## Question

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.
In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

### Example 1:

```java
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2:

```java
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

### Constraints:

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Algorithm

- Create a HashMap of `s1` (character by occurrence)
- For each substring of `s2` ((0, s1.length), (1, s1.length +1), … (s2.length - s1.length, s2.length))
  - Create a HashMap of the substring (character by occurrence)
  - If the substring map == the s1 map return true
- Return false

## Code

```java

class Solution {

    public boolean checkInclusion(String s1, String s2) {

        Map<Character, Integer> map = new HashMap<>();

  
  

        for (char c : s1.toCharArray())

            map.put(c, map.getOrDefault(c,0)+1);

  

        for (int j =0; j <= s2.length()-s1.length(); j++){

            Map<Character, Integer> map2 = new HashMap<>();

            for (int k = 0; k < s1.length(); k++){

                map2.put(s2.charAt(j + k), map2.getOrDefault(s2.charAt(j + k),0)+1);

            }

  

            if (map.equals(map2))

                return true;

        }

  

        return false;

    }

}
```

## Links

[LeetCode](https://leetcode.com/problems/permutation-in-string/description/)
