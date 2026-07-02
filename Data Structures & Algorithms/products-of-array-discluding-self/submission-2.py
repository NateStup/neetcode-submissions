class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0

        for num in nums:
            if num:
                prod = prod * num
            else:
                zeros += 1
            
        if zeros > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if zeros: res[i] = 0 if num else prod
            else:
                res[i] = int(prod / num)

        return res