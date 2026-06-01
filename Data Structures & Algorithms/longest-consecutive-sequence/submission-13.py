class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        res = 0
        
        for i in range(len(nums)):
            current_sequence_length, current_num = 1, nums[i]
            while current_num + 1 in nums:
                current_sequence_length += 1
                current_num += 1
            res = max(res, current_sequence_length)

        return res