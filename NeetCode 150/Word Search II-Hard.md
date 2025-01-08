## Question
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
### Example 1:



```java
Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]

```
### Example 2:



```java
Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []

```
Constraints:
1 <= board.length, board[i].length <= 10
board[i] consists only of lowercase English letter.
1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.


### Recommended Time & Space Complexity

You should aim for a solution with O(m * n * 4 * (3^(t-1)) + s) time and O(s) space, where m is the number of rows, n is the number of columns, t is the maximum length of any word and s is the sum of the lengths of all the words.






## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/search-for-word-ii)

[LeetCode](https://leetcode.com/problems/search-for-word-ii)
