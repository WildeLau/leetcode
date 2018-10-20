#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (22.13%)
# Total Accepted:    400.3K
# Total Submissions: 1.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                lo, hi, sum = i+1, len(nums)-1, 0-nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == sum:
                        res.append([nums[j] for j in [i, lo, hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < sum:
                        lo += 1
                    else:
                        hi -= 1

        return res


