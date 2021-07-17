class Solution:
    def maxArea(self, height: [int]) -> int:
        """双指针经典题，左右指针相互移动，因为最大的面积一定是一定相对矮的一遍的边界值"""
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            if height[left] < height[right]:
                length = right - left
                result = max(result, length * height[left])
                left += 1
            else:
                length = right - left
                result = max(result, length * height[right])
                right -= 1

        return result


