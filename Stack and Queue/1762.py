class Solution:
    def findBuildings(self, heights: [int]) -> [int]:
        """单调递减的stack，遇到新加入的大于前一个，则前一个pop出去直到前一个大于新加入的"""
        stack = []

        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack

