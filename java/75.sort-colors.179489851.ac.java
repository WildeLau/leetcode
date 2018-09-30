/*
 * [75] Sort Colors
 *
 * https://leetcode.com/problems/sort-colors/description/
 *
 * algorithms
 * Medium (39.98%)
 * Total Accepted:    253.2K
 * Total Submissions: 632.9K
 * Testcase Example:  '[2,0,2,1,1,0]'
 *
 * Given an array with n objects colored red, white or blue, sort them in-place
 * so that objects of the same color are adjacent, with the colors in the order
 * red, white and blue.
 * 
 * Here, we will use the integers 0, 1, and 2 to represent the color red,
 * white, and blue respectively.
 * 
 * Note: You are not suppose to use the library's sort function for this
 * problem.
 * 
 * Example:
 * 
 * 
 * Input: [2,0,2,1,1,0]
 * Output: [0,0,1,1,2,2]
 * 
 * Follow up:
 * 
 * 
 * A rather straight forward solution is a two-pass algorithm using counting
 * sort.
 * First, iterate the array counting number of 0's, 1's, and 2's, then
 * overwrite array with total number of 0's, then 1's and followed by 2's.
 * Could you come up with a one-pass algorithm using only constant space?
 * 
 * 
 */
class Solution {
    public void sortColors(int[] nums) {
        int redEnd = 0;
        int blueStart = nums.length - 1;
        int dichronicEnd = 0;
        
        while (dichronicEnd <= blueStart) {
            // Mantaining the definition of the three index.
            switch (nums[dichronicEnd]) {
                case 0: nums[dichronicEnd] = nums[redEnd];
                        nums[redEnd] = 0;
                        redEnd += 1;
                        dichronicEnd += 1;
                        break;
                case 1: dichronicEnd += 1;
                        break;
                case 2: nums[dichronicEnd] = nums[blueStart];
                        nums[blueStart] = 2;
                        blueStart -= 1;
                        break;
                default: break;
            }
        }
    }
}

