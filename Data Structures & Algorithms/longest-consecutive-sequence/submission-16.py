class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            curr_seq, curr_num = 1, num
            while curr_num + 1 in nums:
                curr_seq += 1
                curr_num += 1
            res = max(res, curr_seq)

        return res