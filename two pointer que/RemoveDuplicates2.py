'''
You're given a list of integers already sorted in non-decreasing order.

Trim it down so that every distinct value appears at most twice, while keeping the remaining elements in their original (sorted) relative order, and return the trimmed list.

The classic in-place version of this problem cares about not using extra space and reporting a count, but for this exercise just return the resulting list directly.

Input: nums = [1,1,1,2,2,3]
Output: [1,1,2,2,3]
the third 1 is dropped since 1 already appears twice; everything else appears at most twice already
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: [0,0,1,1,2,3,3]
1 appears four times in the input, so the third and fourth copies are dropped, leaving exactly two
Input: nums = [1,2,3]
Output: [1,2,3]
no value repeats more than twice, so nothing is removed
Constraints
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order
'''

def removeDuplicates(nums):
    write = 0

    for read in range(len(nums)):
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    del nums[write:]
    return nums


arr=[1,1,1,2,2,3,3]

print(removeDuplicates(arr))