class Solution1:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n // 5 > 0:
            n //= 5
            ans += n

        return ans


class Solution2:
    def trailingZeroes(self, n: int) -> int:
        """递归写法，每次传入的是 n // 5之后的除数"""
        if n == 0:
            return 0

        ans = self.trailingZeroes(n // 5)

        return n // 5 + ans



