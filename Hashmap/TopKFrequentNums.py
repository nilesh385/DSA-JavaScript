'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''

def topKFrequent(nums,k):
    freMap=dict()
    res=[]

    for i in range(len(nums)):
        if not freMap.get(nums[i]):
            freMap[nums[i]]=1
        else:
            freMap[nums[i]]= freMap.get(nums[i])+1

    # create n number of buckets, where n is the length of nums
    buckets= [[] for _ in range(len(nums)+1)]

    # fill the bucket values according to the freq
    for num,freq in freMap.items():
        buckets[freq].append(num)

    for i in range(len(buckets)-1,0,-1):# start,end,gap. gap is -1 because we are moving backwards

        # one bucket/freq can be multiple nums
        for num in buckets[i]:
            res.append(num)

            if len(res)==k:
                return res