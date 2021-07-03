class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        贪心和stack的结合思维
        当遇到更小的数据时，提出前面的数据直到前一个小于当前数字，0不用压进stack作为开头，因为我们最后都要抛弃0作为开头
        如果k没有用完，就从后向前剔除，因为后面的一定大于前面的数字
        :param num:
        :param k:
        :return:
        """
        if k == len(num):
            return '0'

        stack = []
        for i in num:
            while len(stack) > 0 and int(i) < int(stack[-1]) and k > 0:     # 剔除前一个直到小于当前数字
                stack.pop()
                k -= 1

            if len(stack) == 0 and i == '0':        # 0作为第一个不需要进入stack
                continue

            stack.append(str(i))

        while k > 0 and len(stack) > 0:     # 如果有多的数字需要剔除
            stack.pop()
            k -= 1

        if len(stack) == 0:     # 考虑剔除后为空的情况
            return '0'
        else:
            return "".join(stack)