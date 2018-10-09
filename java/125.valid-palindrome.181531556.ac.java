/*
 * [125] Valid Palindrome
 *
 * https://leetcode.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (28.65%)
 * Total Accepted:    271.2K
 * Total Submissions: 946K
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * Given a string, determine if it is a palindrome, considering only
 * alphanumeric characters and ignoring cases.
 * 
 * Note: For the purpose of this problem, we define empty string as valid
 * palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: "A man, a plan, a canal: Panama"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "race a car"
 * Output: false
 * 
 * 
 */
class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;
        s = s.toLowerCase();
        boolean result = true;
        while (start < end) {
            while (!Character.isLetterOrDigit(s.charAt(start)) && start < end)
                start += 1;
            while (!Character.isLetterOrDigit(s.charAt(end)) && start < end)
                end -= 1;
            if (s.charAt(start) != s.charAt(end)){
                result = false;
                break;
            }
            start += 1;
            end -= 1;
        }

        return result;
    }
}

