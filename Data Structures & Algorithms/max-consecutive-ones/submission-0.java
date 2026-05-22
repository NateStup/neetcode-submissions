class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int longest = 0;
        int current = 0;
        for(int i = 0; i < nums.length; i++){
            if (nums[i] == 0){
                current = 0;
            }
            else{
                current += 1;
            }
            if (longest < current){
                longest = current;
            }
            }
            return longest;
        }
    }