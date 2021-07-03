class Solution:
    def findMaxForm(self, strs: [str], m: int, n: int) -> int:
        """
        本题中strs 数组里的元素就是物品，每个物品都是一个！ 而m 和 n相当于是一个背包，两个维度的背包。
        dp[i][j]：最多有i个0和j个1的strs的最大子集的大小为dp[i][j]。
        所以递推公式：dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1);
        这里表示此时的最大容量（多少个元素子集里面）为当前容量减去当前物品及str有多少个0和多少个1的时候的容量 + 此时这个物品及str

        对比0-1背包的模板发现，字符串的zeroNum和oneNum相当于物品的重量（weight[i]），字符串本身的个数相当于物品的价值（value[i]）。
        :param strs:
        :param m:
        :param n:
        :return:
        """
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for s in strs:
            one_number = 0
            zero_number = 0
            for ss in s:
                if ss == '0':
                    zero_number += 1
                else:
                    one_number += 1
            for i in range(m, zero_number - 1, -1):
                for j in range(n, one_number - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_number][j - one_number] + 1)

        return dp[m][n]


s = Solution()
print(s.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
