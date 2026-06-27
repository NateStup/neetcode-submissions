class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set()
        for i in range(len(nums)):
            numbers.add(i + 1)

        for num in nums:
            numbers.discard(num)
        
        return list(numbers)