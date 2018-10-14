#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (42.90%)
# Total Accepted:    187.5K
# Total Submissions: 436.7K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
#
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        result = False
        sum = n
        sum_set = set()
        while sum not in sum_set:
            sum_set.add(sum)
            n = sum
            sum = 0
            while n > 0:
                sum += pow(n % 10, 2)
                n = n // 10
            if sum == 1:
                result = True
                break

        return result

