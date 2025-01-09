---
date created: 2025-01-09 16:34
date updated: 2025-01-09 16:42
---

Tags: [[Array]] [[Prefix Sum]]
Similar Questions: 
## Question

Given an integer array `nums`, return an array output where `output[i]` is the product of all the elements of `nums` except `nums[i]`.
Each product is guaranteed to fit in a 32-bit integer.

### Example 1:

```java
Input: nums = [1,2,4,6]

Output: [48,24,12,8]

```

### Example 2:

```java
Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

```

### Constraints:

`2 <= nums.length <= 1000`
`-20 <= nums[i] <= 20`

### Recommended Time & Space Complexity

You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

## Algorithm
- Iterate over `nums` and keep track of 3 variables 
	- Max: current product of a elements 
	- MaxNonZero: current product of a elements (excluding elements equal to 0)
	- Zeros: number of elements equal to 0 in `nums`
- Iterate over `nums` again updating each value 
	- If zeros > 1 then set the value to 0 
		- This means in every subset where the current number is excluded there is at least 1 zero
	- If the current value == 0 then set the value to MaxNonZero 
		- This is to avoid the divide by 0 error 
	- Otherwise the value is max divided by the current value 
		- `max / nums[i]`
## Code

```java
class Solution {

    public int[] productExceptSelf(int[] nums) {

        int max = 1;

        int maxNonZero =1;

        int zeros =0;

        for (int i : nums ){

            max*=i;

            if (i !=0 ){

                maxNonZero*=i;

            } else {

                zeros++;

            }

        }

        for (int i =0; i < nums.length; i++){

            if (zeros > 1){

                nums[i] = 0;

            } else if (nums[i] != 0 )

                nums[i]=max / nums[i];

            else {

                nums[i] = maxNonZero;

            }

        }

        return nums;

    }

}
```

## Links

[NeetCode](https://neetcode.io/problems/products-of-array-discluding-self)

[LeetCode](https://leetcode.com/problems/encode-and-decode-strings/)
