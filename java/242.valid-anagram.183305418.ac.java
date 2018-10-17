/*
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (48.99%)
 * Total Accepted:    255.4K
 * Total Submissions: 520.2K
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t , write a function to determine if t is an anagram
 * of s.
 * 
 * Example 1:
 * 
 * 
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * 
 * Note:
 * You may assume the string contains only lowercase alphabets.
 * 
 * Follow up:
 * What if the inputs contain unicode characters? How would you adapt your
 * solution to such case?
 * 
 */
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.isEmpty() || t.isEmpty())
            return true;
        HashMap<Character, Integer> letterCounter = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if (letterCounter.containsKey(c))
                letterCounter.put(c, letterCounter.get(c)+1);
            else
                letterCounter.put(c, 1);
        }
        for (int i = 0; i < t.length(); i++) {
            Character c = t.charAt(i);
            if (letterCounter.containsKey(c)) {
                letterCounter.put(c, letterCounter.get(c)-1);
                if (letterCounter.get(c) == 0)
                    letterCounter.remove(c);
            } 
            else
                return false;   
        } 
        
        return letterCounter.size() == 0;   
    }
}

