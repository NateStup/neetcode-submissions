class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(range(1, len(nums) + 1))

        for num in nums:
            numbers.discard(num)
        
        return list(numbers)