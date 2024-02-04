class Solution1:
    def say(self, n):
        # 计数的方法写，不用双指针
        res = ""
        count = 0

        for i in range(len(n)):
            # 如果不是最后一个数
            if i < len(n) - 1:
                # 如果当前和下一个是同一个数
                if n[i] == n[i + 1]:
                    count += 1
                # 如果遇到的下一个和当前这个不一样
                else:
                    count += 1
                    res += str(count) + n[i]
                    count = 0
            # 如果走到最后一个数字
            else:
                # 如果原始string大于1，并且最后一个和前一个相等
                if i > 0 and n[i] == n[i - 1]:
                    count += 1
                    res += str(count) + n[i]
                # 如果原始string等于1或者最后一个和前一个不相等
                else:
                    count = 1
                    res += str(count) + n[i]

        return res

    def countAndSay(self, n: int) -> str:
        """
        Time O(n)
        Space O(n)
        迭代法，从1到最后开始loop，每次的输出是下一个的输入。
        """
        res = "1"
        while n - 1 > 0:
            res = self.say(res)
            n -= 1

        return res


class Solution2:
    def countAndSay(self, n):
        """
        Time O(n)
        Space O(n)
        递归的写法，先写base case，后续遍历的思路，拿到返回值再处理。
        """
        # base case
        if n == 1:
            return '1'

        # 后续遍历递归拿到子节点的返回值
        s = self.countAndSay(n - 1)

        # 双指针写法，i代表左指针
        i = 0
        res = ""
        for j in range(len(s)):
            # 如果当前是最后一个数字或者下一个和当前不相等
            if j == len(s) - 1 or s[j + 1] != s[j]:
                # 双指针计算个数
                res += str(j - i + 1)
                res += s[i]
                # 更新左指针
                i = j + 1
        return res


s = Solution2()
print(s.countAndSay(n=4))
