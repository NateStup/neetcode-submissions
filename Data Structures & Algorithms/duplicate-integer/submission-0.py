class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                if nums[i] == nums[x]:
                    return True
        return False