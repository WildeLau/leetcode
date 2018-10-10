#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (39.92%)
# Total Accepted:    125.7K
# Total Submissions: 314.9K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l, r = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        chars = list(s)
        while l < r:
            while chars[l] not in vowels and l < r:
                l += 1
            while chars[r] not in vowels and l < r:
                r -= 1
            if l >= r:
                break;
            
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1

        return "".join(chars)

