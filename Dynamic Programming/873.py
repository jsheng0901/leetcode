from typing import List


class Solution1:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Time O(n^2 * log(m)) n -> length of arr     m -> max number in arr
        Space O(n)
        确定两个数之后，我们可以找到这两个作为斐波那契数列的下一个数也就是arr[i] + arr[j] = arr[k]，是否存在数组内，
        如果存在则继续向前滚动判断，这个存在的步骤可以采用字典的形式，先记录下来每个元素对应的index，来达到O(1)的时间查存在。
        """
        # 记录元素和index的关系
        val_2_index = {}
        for i, val in enumerate(arr):
            val_2_index[val] = i

        ans = float('-inf')
        # 遍历所有两两组合
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                tmp_length = 0
                tmp_i = i
                tmp_j = j
                # 如果存在则继续判断下一句是否存在
                while arr[tmp_i] + arr[tmp_j] in val_2_index:
                    tmp_length += 1
                    # 下一个index
                    k = val_2_index[arr[tmp_i] + arr[tmp_j]]
                    # 滚动index
                    tmp_i = tmp_j
                    tmp_j = k
                # 记录最大值
                ans = max(ans, tmp_length)

        if ans > 0:
            return ans + 2
        else:
            return ans


class Solution2:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        每组数滚动向前判断的时候，其实我们可以写一个dp来记录。这里重点是状态为一个二维数组。
        定义状态 dp[i][j]表示为：以 arr[i]，arr[j] 为结尾的斐波那契式子序列的最大长度。
        则满足 arr[i] + arr[j] = arr[k]的条件下有，dp[j][k] = max(dp[j][k]，dp[i][j] + 1)
        """
        val_2_index = {}
        for i, val in enumerate(arr):
            val_2_index[val] = i

        ans = 0
        # 初始化所有组合
        dp = [[0] * len(arr) for _ in range(len(arr))]
        # 所有两两组合都可以组成斐波那契数列的最初两个数，所以长度都是2，注意这里只初始化上三角也就是i，j的大小一定是j > i
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                dp[i][j] = 2

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # 判断是否存在下一个数
                if arr[i] + arr[j] in val_2_index:
                    # 下一个数的index
                    k = val_2_index[arr[i] + arr[j]]
                    # 更新下一个数的状态
                    dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                    ans = max(ans, dp[j][k])

        return ans


s = Solution2()
print(s.lenLongestFibSubseq(arr=[1, 3, 7, 11, 12, 14, 18]))
print(s.lenLongestFibSubseq(arr=[1, 2, 3, 4, 5, 6, 7, 8]))
