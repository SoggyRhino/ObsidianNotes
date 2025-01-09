## Question
Design a data structure that supports adding new words and searching for existing words.
Implement the WordDictionary class:
void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
### Example 1:


```java
Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

```
Constraints:
1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.


### Recommended Time & Space Complexity

You should aim for a solution with O(n) time for each function call and O(t + n) space, where n is the length of the string and t is the total number of nodes created in the Trie.





## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/design-word-search-data-structure)

[LeetCode](https://leetcode.com/problems/design-word-search-data-structure)
