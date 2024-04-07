from typing import List


class Solution1:
    def maxArea(self, height: [int]) -> int:
        """
        Time O(n)
        Space O(1)
        双指针经典题，左右指针相互移动，因为最大的面积一定是一定相对矮的一遍的边界值
        """
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


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        一样的思路，换一种写法
        """
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            # 找到最矮的一边高度
            cur_area = min(height[left], height[right]) * (right - left)
            res = max(res, cur_area)
            # 矮的一边进行移动，因为移动后可能会得到更大的面积
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res


s = Solution2()
print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
