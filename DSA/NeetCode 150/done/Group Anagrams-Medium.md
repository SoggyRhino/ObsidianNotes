---
date created: 2025-01-09 16:07
date updated: 2025-01-09 16:14
---

Tags: [[Array]], [[Hash Table]], [[Strings]]
Similar Questions: [[Valid Anagram-Easy]], [[Find Resultant Array After Removing Anagrams-Easy]], [[Count Anagrams-Hard]]

## Question

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:

```java
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

```

### Example 2:

```java
Input: strs = ["x"]

Output: [["x"]]

```

### Example 3:

```java
Input: strs = [""]

Output: [[""]]

```

### Constraints:

`1 <= strs.length <= 1000`
`0 <= strs[i].length <= 100`
`strs[i]` is made up of lowercase English letters.

### Recommended Time & Space Complexity

You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.

## Algorithm

- Anagrams should be equal when you sort a string alphabetically
  - Create a hashmap of sorted key to list of original keys
  - For each string
    - If map has sorted version then add original to the list
    - else create a new key with sorted and list of original
- Instead of sorting each string O(n log(n)) we can create an array where each index is a character and the value at that position is the count then turn the array into a string instead, this uses more memory and only works if we are constrained to a small character set

## Code

```C++
#include <unordered_map>
#include <string>
#include <vector>

class Solution {

public:

    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> result;

        for (const auto & str : strs){
            int keys[26] = {};

            for (auto c : str)
                keys[c - 'a']++;

            std::string key{};
            for (int i =0; i < 26; i++)
                key += keys[i];

            result[key].push_back(str);

        }
        std::vector<std::vector<std::string>> final;

        for (const auto& pair : result)
            final.push_back(std::move(pair.second));
            
        return final;
    }

};
```

## Links

[NeetCode](https://neetcode.io/problems/anagram-groups)

[LeetCode](https://leetcode.com/problems/group-anagrams/)
