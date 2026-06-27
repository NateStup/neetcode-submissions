class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = []
        for i in range(len(nums)):
            numbers.append(i + 1)

        for num in nums:
            if num in numbers:
                numbers.remove(num)
    
        return numbers