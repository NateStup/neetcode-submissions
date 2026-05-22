class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr) - 1):
            greatest = 0
            for y in range(i + 1, len(arr)):
                if arr[y] > greatest:
                    greatest = arr[y]
            arr[i] = greatest
        arr[len(arr) - 1] = -1
        return arr