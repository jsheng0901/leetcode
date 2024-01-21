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


class Solution2:
    def findBuildings(self, heights: [int]) -> [int]:
        """
        Time O(n)
        Space O(1)
        不用栈，一直维护一个当前从右到左的最大值即可，除去输出空间，没有额外空间使用。
        从右向左遍历，如果有当前一个大于目前的最高build，则加入result，最后reverse result， 但需要reverse。
        """
        cur_max = float('-inf')

        result = []

        for i in range(len(heights) - 1, -1, -1):
            # 如果当前高度大于最大高度，说明可以看到海，加入结果
            if heights[i] > cur_max:
                result.append(i)
            # 更新当前最高高度
            cur_max = max(cur_max, heights[i])

        result.reverse()

        return result


s = Solution()
print(s.findBuildings(heights=[4, 2, 3, 1]))
