class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights) - 1):
            left_height = heights[i]
            for j in range(i+1, len(heights)):
                right_height = heights[j]
                total_height = min(left_height, right_height)
                total_length = j - i
                current_area = total_height * total_length
                if current_area > max_area:
                    max_area = current_area

        return max_area