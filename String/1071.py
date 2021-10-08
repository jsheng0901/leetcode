class Solution:
    def gcd(self, a, b):
        """找两个数的最大公约数的算法"""
        if b == 0:
            return a

        return b if a % b == 0 else self.gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """如果想加后不相等，则说明没有公约子序列，之后用数学的方法找最大公约数，然后判断子序列"""
        if str1 + str2 != str2 + str1:
            return ""

        length1 = len(str1)
        length2 = len(str2)

        gcd = self.gcd(length1, length2)

        if length1 < length2:
            return str2[:gcd]
        else:
            return str1[:gcd]


