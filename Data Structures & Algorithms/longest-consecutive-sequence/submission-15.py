class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            current_sequence, current_num = 1, num
            while current_num + 1 in nums:
                current_sequence += 1
                current_num += 1
            res = max(res, current_sequence)
            
                
        return res