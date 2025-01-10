---
date created: 2025-01-09 17:50
---

## Code

```java
class Solution {

    public int maxArea(int[] height) {

        int left = 0;

        int right = height.length-1;

  

        int max =0;

  
  

        while (left < right){

            int h1 = height[left];

            int h2 = height[right];

            max = Math.max(max,(right - left) * Math.min(h1, h2));

  

            if (h1 < h2){

                left++;

            } else {

                right--;

            }

        }

        return max;

    }

}

```


[NeetCode](https://neetcode.io/problems/max-water-container)


