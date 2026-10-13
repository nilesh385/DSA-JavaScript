'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

​​​​​​​Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''

def maxSubarrayProduct(nums):
    max_end=nums[0]
    min_end=nums[0]
    res=nums[0]

    for i in range(1,len(nums)):
        v1= nums[i]
        v2=min_end*nums[i]
        v3=max_end*nums[i]
        min_end=min(v1,min(v2,v3))        
        max_end=max(v1,max(v2,v3))       
        res=max(res,max(min_end,max_end))

    return res