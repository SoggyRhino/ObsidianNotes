## Question
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.
You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.
Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.
A string a is lexicographically smaller than a string b if either of the following is true:
The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
### Example 1:


```java
Input: ["z","o"]

Output: "zo"

```
Explanation:From "z" and "o", we know 'z' < 'o', so return "zo".
### Example 2:


```java
Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"

```
Explanation:
from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:
The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100


### Recommended Time & Space Complexity

You should aim for a solution with O(N + V + E) time and O(V + E) space, where N is the sum of the lengths of all the strings, V is the number of unique characters (vertices), and E is the number of edges.






## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/foreign-dictionary)

[LeetCode](https://leetcode.com/problems/foreign-dictionary)
