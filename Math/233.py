class Solution1:
    def count_one(self, n):
        # 计算有多少个1对于一个数n
        string_n = str(n)
        count = 0

        for c in string_n:
            if c == '1':
                count += 1

        return count

    def countDigitOne(self, n: int) -> int:
        """
        Time O(n)
        Space O(1)
        每个逐一进行计算叠加个数，明显会TLE。
        """
        total = 0

        while n > 0:
            total += self.count_one(n)
            n -= 1

        return total


class Solution2:
    def countDigitOne(self, n: int) -> int:
        """
        Time O(n)
        Space O(n)
        DP的思路，对于一个数有多少个1，可以由最高位是否是1 + 余数有多少个1构成，省去了每个数要loop一次找1的时间，但是还是太慢了。并且需要
        额外的O(n) space。
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            i_length = len(str(i))
            remainder = i % (10 ** (i_length - 1))
            divisor = i // (10 ** (i_length - 1))
            add_one = 1 if divisor == 1 else 0
            dp[i] = add_one + dp[remainder]

        return sum(dp)


class Solution3:
    def countDigitOne(self, n: int) -> int:
        """
        Time O(log10(n))
        Space O(1)
        数学公式计算，找规律，详细参考 https://leetcode.com/problems/number-of-digit-one/editorial/
        """
        count = 0
        multiplier = 1
        while multiplier <= n:
            divider = multiplier * 10
            # 公式在这里应用
            count += (n // divider) * multiplier
            count += min(max(n % divider - multiplier + 1, 0), multiplier)
            multiplier *= 10

        return count


s = Solution3()
print(s.countDigitOne(n=13))
print(s.countDigitOne(n=0))
print(s.countDigitOne(n=824883294))
