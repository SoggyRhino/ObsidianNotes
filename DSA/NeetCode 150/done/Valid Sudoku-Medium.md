---
date created: 2025-01-09 16:50
---
Tags: [[Array]], [[Hash Table]], [[Matrix]]
Similar Questions: [[Sudoku Solver-Hard]], [[Check if Every Row and Column Contains All Numbers-Easy]]
## Question

You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
Note: A board does not need to be full or be solvable to be valid.

### Example 1:

```java
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

```

### Example 2:

```java
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

```

Explanation: There are two 1's in the top-left 3x3 sub-box.

### Constraints:
`board.length == 9`
`board[i].length == 9`
`board[i][j]` is a digit `1-9` or `.`

### Recommended Time & Space Complexity

You should aim for a solution as good or better than O(n^2) time and O(n^2) space, where n is the number of rows in the square grid.

## Algorithm
- Has Duplicates helper function (takes in an array of values)
	- Create an array of size 9 to act as a set 
	- For each value of the array 
		- Skip over `.` characters (empty space)
		- If the value in the set is not zero return true 
			- Subtract '0' to get the relative indexes of characters 0-9
		- Add the current character to the set 
			- Set the value at character - '0' to 1 
- Check all rows of `board`
	- If any have duplicates return false
- Check all columns of `board`
	- If any have duplicates return false
-  Check all squares of `board`
	- If any have duplicates return false
## Code

```java
class Solution {

    public  boolean isValidSudoku(char[][] board) {

        for (char[] row : board)

            if (hasDuplicates(row))

                return false;

        for (int i = 0; i < 9; i++) {

            char[] column = new char[9];

            for (int j = 0; j < 9; j++) {

                column[j] = board[j][i];

            }

            if (hasDuplicates(column))

                return false;

        }

        for (int i = 0; i < 9; i += 3) {

            for (int j = 0; j < 9; j += 3) {

                char[] square = new char[]{

                        board[i][j], board[i][j + 1], board[i][j + 2],

                        board[i + 1][j], board[i + 1][j + 1], board[i + 1][j + 2],

                        board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]

                };

                if (hasDuplicates(square))

                    return false;

            }

        }

        return true;

    }

  

    public  boolean hasDuplicates(char[] row) {

        int[] set = new int[9];

        for (char c : row)

            if (c != '.')

                if (set[c - 49] != 0)

                    return true;

                else set[c - 49] =-1;

  

        return false;

    }

}
```
## Links

[NeetCode](https://neetcode.io/problems/valid-sudoku)

[LeetCode](https://leetcode.com/problems/valid-sudoku)


