class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        uniqueNums = set(nums)
        
        return len(nums) != len(uniqueNums)
