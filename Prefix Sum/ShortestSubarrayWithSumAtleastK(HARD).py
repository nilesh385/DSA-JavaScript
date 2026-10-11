'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
-105 <= nums[i] <= 10^5
1 <= k <= 10^9
'''
from collections import deque
def shortestSubarrayK(nums,k):
    res=float('inf')
    dq=deque([(0,0)]) # add prefix sum and its index+1 , because 0th index is already assigned.
    prefix=0

    for i in range(len(nums)):
        prefix+=nums[i]

        while dq and prefix-dq[0][0]>=k:
            idx=dq[0][1]
            lenn=i+1-idx
            res= min(res,lenn)
            dq.popleft()

        while dq and dq[-1][0]>=prefix:
            dq.pop()
        

        dq.append((prefix,i+1)) # i+1 because we have already stored for 0th index, so we will start storing from 1st index


    return -1 if res==float('inf') else res

        