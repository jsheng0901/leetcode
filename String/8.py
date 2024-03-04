class Solution:
    def myAtoi(self, str: str) -> int:
        """
        Time O(n)
        Space O(1)
        基本上没什么特殊方法，按照题目意思注意解释，详细见注释。
        """
        n = len(str)
        i = 0
        # 记录正负号
        sign = 1
        res = 0
        # 记录是否溢出
        over = False
        # 跳过前导空格
        while i < n and str[i] == ' ':
            i += 1
        if i == n:
            return 0

        # 记录符号位
        if str[i] == '-':
            sign = -1
            i += 1
        elif str[i] == '+':
            i += 1
        if i == n:
            return 0

        # 统计数字位
        while i < n and '0' <= str[i] <= '9':
            res = res * 10 + ord(str[i]) - ord('0')
            if res > 2 ** 31 - 1:
                over = True
            i += 1

        # 如果溢出，强转成 int 就会和真实值不同
        if over:
            return sign * (2 ** 31 - 1) if sign == 1 else -2 ** 31

        return int(res) * sign


s = Solution()
print(s.myAtoi(str="   -42"))
print(s.myAtoi(str="4193 with words"))
