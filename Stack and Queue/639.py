class Solution:
    def exclusiveTime(self, n: int, logs: [str]) -> [int]:
        """
        if it's start then put in stack, if it's end, which mean we need finish one function.
        then we pop out last executing function and calculate time
        """
        stack = []
        res = [0] * n

        for i in logs:
            item = i.split(':')
            if item[1] == 'start':
                stack.append(item)
            else:
                top = stack.pop()
                time = int(item[2]) - int(top[2]) + 1
                res[int(top[0])] += time
                if len(stack) > 0:      # this is for minus previous running function executing time
                    res[int(stack[-1][0])] -= time

        return res
