/*
 * [345] Reverse Vowels of a String
 *
 * https://leetcode.com/problems/reverse-vowels-of-a-string/description/
 *
 * algorithms
 * Easy (39.92%)
 * Total Accepted:    125.7K
 * Total Submissions: 314.9K
 * Testcase Example:  '"hello"'
 *
 * Write a function that takes a string as input and reverse only the vowels of
 * a string.
 * 
 * Example 1:
 * 
 * 
 * Input: "hello"
 * Output: "holle"
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "leetcode"
 * Output: "leotcede"
 * 
 * 
 * Note:
 * The vowels does not include the letter "y".
 * 
 * 
 * 
 */
class Solution {
    public String reverseVowels(String s) {
        StringBuilder str = new StringBuilder(s);
        String vowels = new String("aeiouAEIOU");
        int l = 0;
        int r = str.length() - 1;
        while (l < r){
            while (vowels.indexOf(str.charAt(l)) < 0 && l < r)
                l++;
            while (vowels.indexOf(str.charAt(r)) < 0 && l < r)
                r--;
            if (l >= r)
                break;
            char tmp = str.charAt(l);
            str.setCharAt(l++, str.charAt(r));
            str.setCharAt(r--, tmp);
        }

        return str.toString();
    }
}

