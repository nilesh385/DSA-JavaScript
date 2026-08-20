/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 
*/

const minSubArrayLen = function (target, nums) {
    let low = 0;
    let high = 0;
    let res = Infinity;
    let sum = 0;

    while (high < nums.length) {
        sum = sum + nums[high];

        while (sum >= target) {
            let len = high - low + 1;
            res = Math.min(len, res);
            sum -= nums[low];
            low++;
        }
        high++;
    }
    if (res === Infinity) return 0;
    return res;
};
