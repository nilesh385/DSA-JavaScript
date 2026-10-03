'''
You're given two lists of integers, nums1 and nums2, each already
sorted in ascending order.

Return a single list containing all the numbers from both, still sorted in ascending order.

Input: nums1 = [1, 2, 3], nums2 = [2, 5, 6]
Output: [1, 2, 2, 3, 5, 6]
Input: nums1 = [], nums2 = [1]
Output: [1]
Input: nums1 = [1], nums2 = []
Output: [1]
Constraints
0 <= nums1.length, nums2.length <= 200
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 are each sorted in ascending order
'''

def merge(nums1, nums2):
    mergedArr= []
    left=0
    right=0

    while left<len(nums1) and right<len(nums2):
        if nums1[left]<nums2[right]:
            mergedArr.append(nums1[left])
            left+=1
        else :
            mergedArr.append(nums2[right])
            right+=1

    while left<len(nums1):
        mergedArr.append(nums1[left])
        left+=1

    while right<len(nums2):
        mergedArr.append(nums2[right])
        right+=1

    return mergedArr

nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
print(merge(nums1,nums2))