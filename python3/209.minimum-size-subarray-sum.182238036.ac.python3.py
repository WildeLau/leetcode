#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (33.23%)
# Total Accepted:    141.6K
# Total Submissions: 425.7K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        l, r = 0, 0
        min_len = len(nums) + 1
        sum = 0
        while r < len(nums):
            sum += nums[r]
            r += 1

            while sum >= s:
                min_len = min(min_len, r-l)
                sum -= nums[l]
                l += 1
        if min_len > len(nums):
            min_len = 0

        return min_len

