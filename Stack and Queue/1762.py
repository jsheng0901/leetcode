class Solution:
    def findBuildings(self, heights: [int]) -> [int]:
        """
        Time O(n)
        Space O(n)
        从栈底到栈顶单调递减的stack，遇到新加入的大于栈顶元素，则栈顶pop出去直到当前栈顶元素大于新加入的
        """
        stack = []

        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack


s = Solution()
print(s.findBuildings(heights=[4, 2, 3, 1]))
