/*
 * [215] Kth Largest Element in an Array
 *
 * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (42.87%)
 * Total Accepted:    257.6K
 * Total Submissions: 600K
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * Find the kth largest element in an unsorted array. Note that it is the kth
 * largest element in the sorted order, not the kth distinct element.
 * 
 * Example 1:
 * 
 * 
 * Input: [3,2,1,5,6,4] and k = 2
 * Output: 5
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,2,3,1,2,4,5,5,6] and k = 4
 * Output: 4
 * 
 * Note: 
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 * 
 */
class Solution {
    public int findKthLargest(int[] nums, int k) {
        /*
           The 3 steps of quick sort:
           1. Select a pivot;
           2. Portion;
           3. Recursive
        */
        
        int start = 0;
        int end = nums.length - 1;
        int pivotIndex = -1;
        while (pivotIndex != (k - 1)) {
            pivotIndex = partition(nums, start, end);
            if (pivotIndex < (k - 1)) 
                start = pivotIndex + 1;
            if (pivotIndex > (k - 1))
                end = pivotIndex - 1;
        }
        
        return nums[k-1];        
    }

    private int partition(int[] nums, int start, int end) {
        int pivot = nums[end];
        int pivotIndex = start - 1;
        for (int j = start; j < end; j++) {
            if (nums[j] > pivot) {
                pivotIndex += 1;
                swap(nums, j, pivotIndex);    
            }
        }
        pivotIndex += 1;
        swap(nums, pivotIndex, end);

        return pivotIndex;
    }
    
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

}

