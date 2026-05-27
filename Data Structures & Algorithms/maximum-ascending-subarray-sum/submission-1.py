class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = nums[0]
        maxSum = temp
        for i in range(1, len(nums)):
            if (nums[i-1] < nums[i]):
                temp += nums[i]
            else:
                temp = nums[i]
            maxSum = max(temp, maxSum)
        return maxSum