from collections import deque
from typing import List


class Solution1:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        单调栈的思路，这里和找下一个更大的数字的逻辑有点不一样。我们需要的是单调栈内从后向前遍历有多少个比当前数小的数，记录进结果。
        """
        if len(heights) == 0:
            return [0]

        ans = [0] * len(heights)
        stack = deque()

        # 从后向前遍历
        for i in range(len(heights) - 1, -1, -1):
            # 如果当前数更大，说明栈顶的数可以被看到
            while stack and stack[-1] < heights[i]:
                # 当前数对应的index，计数器 +1
                ans[i] += 1
                # 弹出
                stack.pop()
            # 如果栈内还有数，说明遇到了当前数下一个更大的数，也就是边界
            if stack:
                # 计数 +1
                ans[i] += 1
            # 当前数入栈
            stack.append(heights[i])
        return ans


class Solution2:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        思路同上，但是换个方向从前往后找。
        """
        if len(heights) == 0:
            return [0]

        ans = [0] * len(heights)
        stack = deque()
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                # 当前栈顶弹出的数遇到了更大的数，栈顶的index +1
                ans[stack.pop()] += 1

            # 如果栈还存在，说明此时栈顶的数大于当前数，也就是说明栈顶的数看得到这个更小的数，栈顶的index +1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)

        return ans


s = Solution2()
print(s.canSeePersonsCount(heights=[10, 6, 8, 5, 11, 9]))
