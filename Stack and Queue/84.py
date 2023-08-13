class Solution:
    def largestRectangleArea1(self, heights: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        单调递减栈，栈头->栈尾从大到小, 当遇到当前元素小于栈顶元素的时候就开始计算面积，需要最小左边的index和最小右边index
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

    def largestRectangleArea2(self, heights: [int]) -> int:
        """
        三种情况分开写的方法，更直观
        找每个柱子左右侧的第一个高度值小于该柱子的柱子
        单调栈：栈顶到栈底：从大到小（每插入一个新的小数值时，都要弹出先前的大数值）
        栈顶，栈顶的下一个元素，即将入栈的元素：这三个元素组成了最大面积的高度和宽度
        情况一：当前遍历的元素heights[i]大于栈顶元素的情况
        情况二：当前遍历的元素heights[i]等于栈顶元素的情况
        情况三：当前遍历的元素heights[i]小于栈顶元素的情况
        """
        result = 0
        stack = [0]
        # 输入数组首尾各补上一个0（与42.接雨水不同的是，本题原首尾的两个柱子可以作为核心柱进行最大面积尝试）
        heights.insert(0, 0)
        heights.append(0)

        for i in range(1, len(heights)):
            # 情况一
            if heights[stack[-1]] < heights[i]:
                stack.append(i)
            # 情况二
            elif heights[stack[-1]] == heights[i]:
                stack.pop()
                stack.append(i)
            # 情况三
            else:
                # 抛出所有较高的柱子
                while stack and heights[stack[-1]] > heights[i]:
                    # 栈顶就是中间的柱子，此时需要计算面积的高度
                    top = stack.pop()
                    if stack:
                        left = stack[-1]
                        h = heights[top]
                        # 此处计算宽度的方式必须要最小左边的index，最小右边index和当前栈顶元素，因为有[1,1]这种情况
                        w = i - left - 1
                        result = max(result, h * w)

                stack.append(i)

        return result

