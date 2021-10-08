class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        """
        O(n) time, O(n) space
        单调栈，栈头->栈尾从大到小, 当遇到当前元素小于栈顶元素的时候就开始半段面积，需要最小左边的index和最小右边index
        """
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:        # 开始计算面积
                tmp = stack[-1]
                stack.pop()
                if stack:           # 有可能没有左边的index，需要判断
                    min_right_index = i
                    min_left_index = stack[-1]
                    w = min_right_index - min_left_index - 1
                    h = heights[tmp]
                    result = max(result, w * h)
            stack.append(i)

        return result

