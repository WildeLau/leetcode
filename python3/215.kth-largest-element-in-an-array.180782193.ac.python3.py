#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (42.87%)
# Total Accepted:    257.6K
# Total Submissions: 600K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
       
        start = 0
        end = len(nums) - 1
        pivot_index = -1
        while pivot_index != (k - 1):
            pivot_index = self.portion(nums, start, end)
            if pivot_index > (k - 1):
                end = pivot_index - 1
            if pivot_index < (k - 1):
                start = pivot_index + 1

        return nums[k - 1]

    def portion(self, nums, start, end):

        pivot = nums[end]
        pivot_index = start
        for i in range(start, end):
            if nums[i] > pivot:
                nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
                pivot_index += 1
        
        nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

        return pivot_index

