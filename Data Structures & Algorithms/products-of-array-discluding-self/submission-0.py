class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)): # represents the index of the new array
            product = 1
            for j in range(len(nums)): # represents the index of nums
                if i != j:
                    product = product * nums[j]
            res.append(product)
        return res