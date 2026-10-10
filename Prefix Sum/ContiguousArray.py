'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

def findMaxLen(nums):
    one=0
    zero=0
    res=0
    left=0
    right=0

    while right<len(nums):
        if nums[right]==0:zero+=1
        else: one+=1

        while one==zero:
            lenn=right-left+1
            res= max(res,lenn)

            if nums[left]==0: zero-=1
            else: one-=1
            low+=1

        right+=1

    return res