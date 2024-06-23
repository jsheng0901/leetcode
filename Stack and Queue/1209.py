class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Time O(n)
        Space O(n)
        利用栈的特性，查看栈顶元素是否和当前元素相等，如果相等更新频率，如果频率等于k，说明可以开始弹出栈顶元素直到不相等，遇到不相等的元素
        直接加入栈同时频率为1，最后我们只需要把栈内剩余的元素全部拼起来就好了，注意用loop拼，不要用栈弹出拼接，因为弹出栈底不是O(1)操作。
        """
        # 记录出现元素和频率
        stack = []

        for c in s:
            # 如果栈顶元素和当前元素一样
            if stack and stack[-1][0] == c:
                # 栈顶元素的频率
                count = stack[-1][1]
                # 如果加上当前这个元素后频率和k一样
                if count + 1 == k:
                    # 开始弹出栈顶所有一样的元素
                    while stack and stack[-1][0] == c:
                        stack.pop()
                # 如果频率相加后小于k，新的元素加入栈并更新频率
                else:
                    stack.append((c, count + 1))
            # 如果没有元素或者元素不一样，都是直接加入栈并且频率为1
            else:
                stack.append((c, 1))

        # 重新构建栈内所有剩下的元素
        res = ''
        for s in stack:
            res += s[0]

        return res


s = Solution()
print(s.removeDuplicates(s="abcd", k=2))
print(s.removeDuplicates(s="deeedbbcccbdaa", k=3))
