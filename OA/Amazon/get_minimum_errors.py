# 2024-05-12
# Amazon's database doesn’t support very large numbers, so numbers are stored as a string of binary characters,
# '0' and '1'. Accidentally, a '!' was entered at some positions and it is unknown whether they should be '0' or '1'.
#
# The string of incorrect data is made up of the characters '0', '1' and '!' where '!' is the character that got
# entered incorrectly. '!' can be replaced with either '0' or '1'. Due to some internal faults, some errors are
# generated every time '0' and '1' occur together as '01' or '10' in any subsequence of the string. It is observed
# that the number of errors a subsequence '01' generates is x, while a subsequence '10' generates y errors.
#
# Determine the minimum total errors generated. Since the answer can be very large, return it modulo 109+7.
#
# Note: A subsequence of a string is obtained by omitting zero or more characters from the original string without
# changing their order.
#
# Hint: It can be proved that (a + b) % c = ((a% c) + (b % c)) % c where a, b, and c are integers and % represents
# the modulo operation.
#
# Function Description
#
# Complete the function getMinErrors in the editor.
#
# getMinErrors has the following parameter(s):
#
# String errorString: a string of characters '0', '1', and '!'
# int x: the number of errors generated for every occurrence of subsequence 01
# int y: the number of errors generated for every occurrence of subsequence 10
# Returns
#
# int: the minimum number of errors possible, modulo 10^9+7


class Solution:
    def getMinErrors(self, errorString: str, x: int, y: int) -> int:
        """
        Time O(n)
        Space O(n)
        DP的思路，每次当前最小的error其实和前一位的最小error有关系，当前位是0或者1刚好影响 01 或者 10 的个数，只需要一直记录走到当前位置
        的时候两种情况的个数，即可通过前一个位置的error叠加得到当前的error数。如果遇到 ! 号判断哪一种情况最小error，就选哪一种，贪心思路。
        """
        mod = 10 ** 9 + 7
        n = len(errorString)
        # dp[i] the min errors generated by string errorString[0..i]
        dp = [0] * n
        # 初始化一定是0，因为没有任何x y的个数
        dp[0] = 0
        # 第一个字母是哪一个并计数
        num_0 = 1 if errorString[0] == "0" else 0
        num_1 = 1 if errorString[0] == "1" else 0
        # 从第二个开始遍历
        for i in range(1, n):
            # 当前字母
            c = errorString[i]
            # 如果是0，说明1的个数就是多出来可以和当前这个0构成y的个数
            if c == "0":
                dp[i] = dp[i - 1] + num_1 * y
                # 0的个数叠加
                num_0 += 1
            # 如果是1，说明0的个数就是多出来可以和当前这个1构成x的个数
            elif c == "1":
                dp[i] = dp[i - 1] + num_0 * x
                # 1的个数叠加
                num_1 += 1
            # 如果是 ! 号
            else:
                # 第一种情况，当前y的更少，选择变成0
                if num_1 * y <= num_0 * x:
                    dp[i] = dp[i - 1] + num_1 * y
                    num_0 += 1
                # 第二种情况，当前x的更少，选择变成1
                else:
                    dp[i] = dp[i - 1] + num_0 * x
                    num_1 += 1

        return dp[-1] % mod


s = Solution()
print(s.getMinErrors(errorString="101!1", x=2, y=3))
print(s.getMinErrors(errorString="01!0", x=2, y=2))
print(s.getMinErrors(errorString="!!!!!!!", x=23, y=27))