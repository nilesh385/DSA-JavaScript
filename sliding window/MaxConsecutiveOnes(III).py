'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
 

'''

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        low=0
        zeroes=0
        res=0

        for high in range(len(nums)):
            if nums[high]==0:
                zeroes+=1
            while zeroes>k:
                if nums[low]==0:
                    zeroes-=1
                low+=1

            lenn=high-low+1
            res=max(res,lenn)       

        return res            