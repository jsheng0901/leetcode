import math


class Solution:
    def countPrimes(self, n: int) -> int:
        """Sieve of Eratosthenes: loop 每个数字，把这个数字的倍数全部记录下，存进set里面，最后用n减去set的length + 2(1,n)"""
        if n <= 2:
            return 0

        number = set()

        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in number:
                for m in range(i * i, n, i):
                    number.add(m)

        return n - len(number) - 2