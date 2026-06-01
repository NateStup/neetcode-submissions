class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count, maxLucky = {}, -1

        for num in arr:
            count[num] = 1 + count.get(num, 0)
        
        for num in count:
            if num == count[num]:
                maxLucky = max(maxLucky, num)
        
        return maxLucky