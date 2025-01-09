---
date created: 2025-01-09 16:27
date updated: 2025-01-09 16:32
---

Tags: [[Strings]]

## Question

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

### Example 1:

```java
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

```

### Example 2:

```java
Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

```

## Constraints:

`0 <= strs.length < 100`
`0 <= strs[i].length < 200`
`strs[i]` contains only UTF-8 characters.

### Recommended Time & Space Complexity

You should aim for a solution with O(m) time and O(1) space for each encode() and decode() call, where m  is the sum of lengths of all the strings.

## Algorithm

### Encode

- Add a prefix to each string containing its length and a separator
  - `string.length()` + `|` + `string`
- Join all strings together
- Note: use a string builder to increase performance 

### Decode

- While `str` has characters
- Parse string length until we reach the separator character `|`
- Read the next `legnth` characters as a string

## Code

```java

class Solution {

    public String encode(List<String> strs) {
        String result = "";
        for (String s: strs)
            result+= s.length() + "|" + s;  
        return result;

    }

    public List<String> decode(String str) {
        List<String> results = new ArrayList<String>();
        for (int i = 0; i < str.length(); ) {
            String length = "";
            for (int j = i; i < str.length(); j++) {
                char c = str.charAt(i++);
                if (c >= '0' && c <= '9')
                    length += c;
                else
                    break;
            }

            int size = Integer.parseInt(length);
            results.add(str.substring(i, i + size));
            i += size;
        }
        return results;
    }
}

```

## Links

[NeetCode](https://neetcode.io/problems/string-encode-and-decode)

LeetCode not available due to paywall