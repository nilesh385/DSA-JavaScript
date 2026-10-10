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
    freq={} # difference of 1 and 0 occurances : index

    for i in range(len(nums)):
        if nums[i]==0:
            zero+=1
        else:
            one+=1
        diff= one-zero

        if diff == 0:
            res= max(res,i+1)
            continue
        if diff in freq:
            last_index= freq.get(diff)
            lenn= i-last_index
            res=max(res,lenn)
        else:
            freq[diff]=i

    return res