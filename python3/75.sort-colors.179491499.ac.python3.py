#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (39.98%)
# Total Accepted:    253.2K
# Total Submissions: 632.9K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       
        red_end = 0
        dichroic_end = 0
        blue_start = len(nums) - 1
       
        while dichroic_end <= blue_start:
            if nums[dichroic_end] == 0:
                nums[dichroic_end], nums[red_end] = nums[red_end], nums[dichroic_end]
                dichroic_end += 1
                red_end += 1
            elif nums[dichroic_end] == 1:
                dichroic_end += 1
            elif nums[dichroic_end] == 2:
                nums[dichroic_end], nums[blue_start] = nums[blue_start], nums[dichroic_end]
                blue_start -= 1
 

