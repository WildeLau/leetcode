#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (28.65%)
# Total Accepted:    271.2K
# Total Submissions: 946K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        front, tail = 0, len(s) - 1
        result = True
        s = s.lower()
        while front < tail:
            while (not s[front].isalnum()) and (front < tail):
                front += 1
            while (not s[tail].isalnum()) and (front < tail):
                tail -= 1
            if s[front] != s[tail]:
                result  = False
                break
            front += 1
            tail -= 1

        return result
                 

