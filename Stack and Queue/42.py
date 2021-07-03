class Solution:
    def trap(self, height: [int]) -> int:
        """
        单调递减stack，当前数字小于stack top数字时候加入stack，遇到当前数字更大的时候，弹出top，计算此时水量，
        这里计算水量要引入弹出后的top，找到最矮的高度，计算宽度，用stack里面加入的index计算
        :param height:
        :return:
        """
        if len(height) < 3:
            return 0

        stack = []
        result = 0

        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] < height[i]:     # 当前数字大于top数字
                top = stack.pop()                                       # 弹出top

                while len(stack) > 0 and height[top] == height[stack[-1]]:  # 如果前一个一模一样，继续弹出top
                    stack.pop()

                if len(stack) > 0:
                    tmp_top = height[stack[-1]]         # 弹出后的top
                    h = min(tmp_top - height[top], height[i] - height[top])     # 弹出后形成的最矮高度
                    w = i - stack[-1] - 1
                    result += h * w

            stack.append(i)

        return result


