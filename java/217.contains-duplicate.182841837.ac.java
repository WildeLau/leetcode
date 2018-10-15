class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set uniqueNums = new HashSet();
        for (int n : nums)
            uniqueNums.add(n);
        
        return nums.length != uniqueNums.size();
    }
}
