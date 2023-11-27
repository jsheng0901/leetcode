from typing import List


class Solution1:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        """
        Time O(n)
        Space O(n)
        三种情况：
            情况一：当前遍历的元素T[i]小于栈顶元素的情况
            情况二：当前遍历的元素T[i]等于栈顶元素的情况
            情况三：当前遍历的元素T[i]大于栈顶元素的情况
        如果求一个元素右边第一个更大元素，单调栈就是递增的，如果求一个元素右边第一个更小元素，单调栈就是递减的。
        这里的递增指的是从栈头到栈底的顺序，及加入数字大于stack[-1]的数字时候开始判断
        单调stack的应用，如果加入stack的数大于stack最后一个数，则弹出最后一个数，并记录此时的index差值到result，
        直到stack最后一个数大于新加入的数，停止loop，继续迭代
        """
        if len(temperatures) == 0:
            return []

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:  # 对应情况3，注意判断栈不能为空
                index = stack.pop()
                result[index] = i - index

            stack.append(i)  # 加入stack的是对应数的index，对应情况1，2

        return result


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        同上原理，反向写单调栈，注意判断条件为当前进入温度大于等于栈顶温度，因为等于的情况下也需要弹出栈顶，我们找的是下一个更大的元素
        """
        stack = []
        # 这里放元素索引，而不是元素
        result = [0] * len(temperatures)
        # 单调栈模板
        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # 得到索引间距
            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result


s = Solution2()
print(s.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
