class Solution:
    def exclusiveTime(self, n: int, logs: [str]) -> [int]:
        """
        Time O(n)
        Space O(n)
        如果是start说明我们开始一个新的程序，直接加入栈。如果是end说明前面有一个程序已经晚上，我们弹出栈顶的程序记录，并计算运行时间，
        加入最终结果，同时我们要为弹出后栈顶的程序对应的运行时间做减法，因为下一个end应该计算运行时间的时候会包括进前面一个程序的运行时间，
        所以我们要提前先减去前一个程序的运行时间。
        """
        stack = []
        res = [0] * n

        for i in logs:
            item = i.split(':')
            # 如果是开始，直接入栈
            if item[1] == 'start':
                stack.append(item)
            # 如果是结束，说明前面有一个程序已经运行完成了
            else:
                top = stack.pop()
                # 计算时间
                time = int(item[2]) - int(top[2]) + 1
                # 更新结束程序的运行时间
                res[int(top[0])] += time
                # 这里很重要，需要减掉前一个程序的运行时间，方便下一个end出现的时候计算运行时间
                if len(stack) > 0:
                    res[int(stack[-1][0])] -= time

        return res


s = Solution()
print(s.exclusiveTime(n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
print(s.exclusiveTime(n=1, logs=["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]))
