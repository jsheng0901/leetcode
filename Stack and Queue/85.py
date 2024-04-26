from typing import List


class Solution1:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        result = 0
        stack = [0]
        heights.insert(0, 0)
        heights.append(0)

        for i in range(1, len(heights)):
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            elif heights[stack[-1]] == heights[i]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    if stack:
                        left = stack[-1]
                        h = heights[top]
                        w = i - left - 1
                        result = max(result, h * w)

                stack.append(i)

        return result

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Time O(m * n + m * n)
        Space O(1)
        此题很巧妙，必须会84题才能想出这个方法。把二位数组转化成一维的histogram来直接应用84题的解法。这里假设每一行都可能是histogram的
        底边，我们需要的是找出每一个底边对应的高度。详细见注释。
        """
        m, n = len(matrix), len(matrix[0])
        # 遍历每一列
        for j in range(n):
            # 对于每一行同一列
            for i in range(m):
                # 如果是1，说明可以有高度
                if matrix[i][j] == "1":
                    # 第一行特殊情况，直接赋值1
                    if i == 0:
                        matrix[i][j] = 1
                    # 其它行如果是1，高度取决于上一行的高度，比如上一行是2，则现在是3，上一行是0，则高度只能是1
                    elif i > 0:
                        matrix[i][j] = matrix[i - 1][j] + 1
                # 如果不是1，说明没有高度，直接赋值0
                else:
                    matrix[i][j] = 0

        max_rectangle = float('-inf')
        # 对于每一行，用之前找到的histogram来计算最大的面积
        for row in range(m):
            # 当前行作为底边的时候的histogram
            heights = matrix[row]
            # 获取最大面积
            area = self.largest_rectangle_area(heights)
            # 记录最大面积
            max_rectangle = max(max_rectangle, area)

        return max_rectangle


class Solution2:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        result = 0
        stack = [0]
        heights.insert(0, 0)
        heights.append(0)

        for i in range(1, len(heights)):
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            elif heights[stack[-1]] == heights[i]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    if stack:
                        left = stack[-1]
                        h = heights[top]
                        w = i - left - 1
                        result = max(result, h * w)

                stack.append(i)

        return result

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Time O(n * m)
        Space O(n)
        一模一样的思路，只是同时计算最大面积的时候，同时更新每一行为底边的histogram。
        """
        m, n = len(matrix), len(matrix[0])

        max_rectangle = float('-inf')
        # 记录每一行是histogram的最大高度
        dp = [0] * n
        for row in range(m):
            for col in range(n):
                # 这里是更新histogram的核心，如果是1，用之前的同一行的状态 + 1，如果不是1，赋值0
                dp[col] = dp[col] + 1 if matrix[row][col] == "1" else 0
            area = self.largest_rectangle_area(dp.copy())
            max_rectangle = max(max_rectangle, area)

        return max_rectangle


s = Solution2()
print(s.maximalRectangle(matrix=[["1", "0"], ["1", "0"]]))
print(s.maximalRectangle(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                 ["1", "0", "0", "1", "0"]]))
