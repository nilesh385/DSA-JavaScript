/*
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
*/

const findUnsortedSubarray = function (nums) {
    let left = 0;
    let right = 0;

    let arr = [...nums];
    arr.sort((a, b) => a - b);
    for (let i = 0; i < nums.length - 1; i++) {
        if (arr[i] !== nums[i]) {
            left = i;
            break;
        }
    }
    for (let j = nums.length - 1; j >= 0; i--) {
        if (arr[i] !== nums[i]) {
            right = i;
            break;
        }
    }

    if (left === 0) return 0;

    return right - left + 1;
};
