/*
 * [209] Minimum Size Subarray Sum
 *
 * https://leetcode.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (33.23%)
 * Total Accepted:    141.6K
 * Total Submissions: 425.7K
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * Given an array of n positive integers and a positive integer s, find the
 * minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
 * one, return 0 instead.
 * 
 * Example: 
 * 
 * 
 * Input: s = 7, nums = [2,3,1,2,4,3]
 * Output: 2
 * Explanation: the subarray [4,3] has the minimal length under the problem
 * constraint.
 * 
 * Follow up:
 * 
 * If you have figured out the O(n) solution, try coding another solution of
 * which the time complexity is O(n log n). 
 * 
 */
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int minLen = 0;
        int sum = 0;
        int start = 0;
        while (minLen < nums.length && sum < s) {
            sum += nums[minLen++];    
        }
        if (sum < s)
            minLen = 0;
        else {
            while (start <= nums.length - minLen) {
                sum -= nums[start++];
                if (sum >= s)
                    minLen -= 1;
                else if (start <= nums.length - minLen) 
                    sum += nums[start + minLen - 1];
                else
                    break;
            }     
        }

        return minLen;
    }
}
