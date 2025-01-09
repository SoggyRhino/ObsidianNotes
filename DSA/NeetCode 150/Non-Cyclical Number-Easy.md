## Question
A non-cyclical number is an integer defined by the following algorithm:
Given a positive integer, replace it with the sum of the squares of its digits.
Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
If it stops at 1, then the number is a non-cyclical number.
Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.
### Example 1:


```java
Input: n = 100

Output: true

```
Explanation: 1^2 + 0^2 + 0^2 = 1
### Example 2:


```java
Input: n = 101

Output: false

```
Explanation:1^2 + 0^2 + 1^2 = 22^2 = 44^2 = 161^2 + 6^2 = 373^2 + 7^2 = 585^2 + 8^2 = 898^2 + 9^2 = 1451^2 + 4^2 + 5^2 = 424^2 + 2^2 = 202^2 + 0^2 = 4 (This number has already been seen)
Constraints:
1 <= n <= 1000


## Algorithm

## Code

## Links

[NeetCode](https://neetcode.io/problems/non-cyclical-number)

[LeetCode](https://leetcode.com/problems/non-cyclical-number)
