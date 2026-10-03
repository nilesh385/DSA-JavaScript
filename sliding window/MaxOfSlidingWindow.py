'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

def maxSlididngWindow(nums,k):
    if len(nums)==1:
        return nums

    low=0
    high=k-1
    res=[]
    secondMax=0

    while high<len(nums):
        # if the res array is empty
        if len(res)==0:
            res.append(max(nums[low:high+1]))
            

        # if the new nums[high] is greater than prev secondMax
        if secondMax<=nums[high]:
            res.append(nums[high])
        else:
            res.append(secondMax)

        for i in range(low,high):
            if nums[i]==res[len(res)-1]:
                continue
            secondMax=max(secondMax,nums[i])
        high+=1
        low+=1
    return res