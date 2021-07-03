class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        """
        单调stack的应用，如果加入stack的数大于stack最后一个数，则弹出最后一个数，并记录此时的index差值到result，
        直到stack最后一个数大于新加入的数，停止loop，继续迭代
        :param temperatures:
        :return:
        """
        if len(temperatures) == 0:
            return []

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index

            stack.append(i)     # 加入stack的是对应数的index

        return result

