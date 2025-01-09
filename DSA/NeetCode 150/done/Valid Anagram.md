---
date created: 2025-01-09 15:21
date updated: 2025-01-09 15:56
---

Tags: [[Array]] [[Hash Table]]
Similar Questions: [[Group Anagrams]], [[Find All Anagrams in a String]], [[Find Resultant Array After Removing Anagrams]]

## Question

Given two strings `s` and `t`, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Example 1:

```java
Input: s = "racecar", t = "carrace"

Output: true

```

### Example 2:

```java
Input: s = "jar", t = "jam"

Output: false

```

### Constraints:

`s` and `t` consist of lowercase English letters.

### Recommended Time & Space Complexity

You should aim for a solution with `O(n + m)` time and `O(1)` space, where n is the length of the string s and m is the length of the string t.

## Algorithm

- If String are not the same length they can not be Anagrams so return early
- Crate a HashMap (in the problem we are constrained to lowercase letters so an array by index(char - 'a' ) is more optimal)
- For each character in String 1 increase the value for key character
- For each character in String 1 decrease the value for key character
- All keys in the map should be 0 since they are used the same number of times in each string

## Code

```java
public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return countS.equals(countT);
    }
}
```

```C++
#include <unordered_map>

#include <string>

class Solution {

  

public:

bool isAnagram(const std::string& s, const std::string& t) {

    int array[26] = {};

  

    for (const auto &item: s)

        array[item - 'a']++;

    for (const auto &item: t)

        array[item - 'a']--;

  

    for(char i = 0; i < 26; i ++)

        if (array[i] != 0)

            return false;

    return true;

}

};
```

## Links

[NeetCode](https://neetcode.io/problems/is-anagram)

[LeetCode](https://leetcode.com/problems/valid-anagram/)




