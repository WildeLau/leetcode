#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (33.32%)
# Total Accepted:    278.7K
# Total Submissions: 834.3K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        tail1 = m - 1
        tail2 = n - 1
        tail = m + n - 1
        while (tail1 >= 0) and (tail2 >= 0):
            if nums1[tail1] > nums2[tail2]:
                nums1[tail] = nums1[tail1]
                tail1 -= 1
            else:
                nums1[tail] = nums2[tail2]
                tail2 -= 1
            tail -= 1
        
        while tail2 >= 0:
            nums1[tail] = nums2[tail2]
            tail -= 1
            tail2 -= 1 

