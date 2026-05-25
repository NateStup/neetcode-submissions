class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        minEven, maxOdd = float('inf'), 0

        for char in s:
            count[char] = 1 + count.get(char, 0)
        
        for counter in count.values():
            if counter % 2 == 1:
                if counter > maxOdd:
                    maxOdd = counter
            elif counter < minEven:
                minEven = counter

        return maxOdd - minEven

            
