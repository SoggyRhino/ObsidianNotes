---
date created: 2025-01-09 15:26
date updated: 2025-01-09 15:37
---

Tags: [[Two Pointers]] [[Strings]]
Similar Questions: [[Palindrome Linked List]], [[Valid Palindrome II]], [[Maximum Product of the Length of Two Palindromic Subsequences]], [[Find First Palindromic String in the Array]], [[Maximum Palindromes After Operations]]
## Question

Given a string `s`, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

### Example 1:

```java
Input: s = "Was it a car or a cat I saw?"

Output: true

```

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

### Example 2:

```java
Input: s = "tab a cat"

Output: false

```

Explanation: "tabacat" is not a palindrome.

### Constraints:

`1 <= s.length <= 1000`
`s` is made up of only printable ASCII characters.

### Recommended Time & Space Complexity

You should aim for a solution with O(n) time and O(1) space, where n is the length of the input string.

## Algorithm

- Start 1 pointer at the index `0` (Left) and 1 at `index length - 1`(right)
- While `left < right`
  - Find the first left character that is a letter
    - If capital change it to lower case (+32)
  - Do the same for the right character
  - If the are not equal return false
- If the loop finishes return true since

## Code

```java
class Solution {

    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            char ci = s.charAt(i);
            if ((!((ci >= 'A' && ci <= 'Z') || (ci >= 'a' && ci <= 'z') || (ci >= '0' && ci <= '9')))) {
               i++;
                continue;
            }
            char cj = s.charAt(j);

            if ((!((cj >= 'A' && cj <= 'Z') || (cj >= 'a' && cj <= 'z') || (cj >= '0'

                    && cj <= '9')))) {

                j--;

                continue;

            }

            if (ci >= 'A' && ci <= 'Z')

                ci+= 32;

            if (cj >= 'A' && cj <= 'Z') {

                cj+= 32;

            }

            if (ci != cj) {

                return false;

            }

            i++;

            j--;

        }

        return true;

    }

}
```

## Links

[NeetCode](https://neetcode.io/problems/is-palindrome)

[LeetCode](https://leetcode.com/problems/valid-palindrome/description/)



