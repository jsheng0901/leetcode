from collections import defaultdict
from typing import List


class Solution1:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        Time O(n^2 * len(duplicate num freq))
        Space O(n)
        参考873的题目，决定下一个数是不是等差数列的重要因素是前面两个数。也就是我们需要找nums[k] - nums[j] = nums[j] - nums[i]
        同样我们可以存储所有数的index对应字典先。这道题难得地方在于等差数列可以是一模一样的数，也就是差值可以是0，同时数组内的数可以是重复的，
        也就是说我们要统计的是所有出现的index要不是最后一个出现的index。找到k的时候找大于j的第一个index，如果不存在则说明没有这个k。
        dp[i][j]表示为：以 nums[i]，nums[j] 为结尾的等差数列的最大长度。
        """
        # 记录所有数出现的对应index
        val_2_index = defaultdict(list)
        for i, val in enumerate(nums):
            val_2_index[val].append(i)

        ans = 2
        # 初始化所有组合
        dp = [[0] * len(nums) for _ in range(len(nums))]
        # 所有两两组合都可以组成等差数列的最初两个数，所以长度都是2，注意这里只初始化上三角也就是i，j的大小一定是j > i
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dp[i][j] = 2

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 差值
                diff = nums[j] - nums[i]
                target = nums[j] + diff
                # 先check是否存在
                if target in val_2_index:
                    # 出现过的所有index里面找第一个大于j的，找到的话说明有下一个等差数列的数
                    target_index = val_2_index[target]
                    for idx in target_index:
                        # 一定是第一个大于j的index
                        if idx > j:
                            k = idx
                            # 更新dp状态
                            dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                            # 更新最大长度
                            ans = max(ans, dp[j][k])
                            break

        return ans


class Solution2:
    def binary_search_right(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > target:
                right = mid - 1
            elif arr[mid] == target:
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1

        # 注意这里output应该是原数组里面对应index的数而不是index本身，如果不存在则输出-1。
        return arr[left] if left < len(arr) else -1

    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        Time O(n^2 * log(len((duplicate num freq)))
        Space O(n)
        同思路1，只是找第一个大于j的index地方我们可以用二分法优化一下，因为同一个数出现的index顺序一定是递增的，然后也就是说我们可以用
        二分法找右边界的方法，找到一个大于j的数在出现过的所有k的index里面。
        二分法找左边界不行，因为左边界会找到等于的情况下的index，而我们要的是大于的情况。
        """
        val_2_index = defaultdict(list)
        for i, val in enumerate(nums):
            val_2_index[val].append(i)

        ans = 2
        # 初始化所有组合
        dp = [[0] * len(nums) for _ in range(len(nums))]
        # 所有两两组合都可以组成等差数列的最初两个数，所以长度都是2，注意这里只初始化上三角也就是i，j的大小一定是j > i
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                dp[i][j] = 2

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                target = nums[j] + diff
                if target in val_2_index:
                    target_index = val_2_index[target]
                    # 区别在这里，用二分法找右边界，第一个大于j的index
                    k = self.binary_search_right(target_index, j)
                    # 如果输出是-1，说明不存在这个k，也就是说明不存在下一个等差数列的数
                    if k != -1:
                        dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                        ans = max(ans, dp[j][k])

        return ans


class Solution3:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        Time O(n^2)
        Space O(n^2)
        换个角度思路，把dp状态改一下，dp[i][diff]表示以nums[i]结尾并且差值为diff的最长等差数列长度，
        这样我们有dp[j][diff] = dp[i][diff] + 1，把差值也放进状态里面去遍历。这样就不用担心重复出现的数。同时dp用字典来记录，因为差值的
        范围不好估计，用二维数组则不好初始化。
        """
        dp = {}

        for i in range(len(nums)):
            for j in range(i):
                # 两个数的差值
                diff = nums[j] - nums[i]
                # 状态转移，如果不存在则j作为等差数列的起点，至少长度为1
                dp[(i, diff)] = dp.get((j, diff), 1) + 1

        # 返回所有可能出现的长度其中的最大值
        return max(dp.values())


s = Solution2()
print(s.longestArithSeqLength(nums=[3, 6, 9, 12]))
print(s.longestArithSeqLength(nums=[9, 4, 7, 2, 10]))
print(s.longestArithSeqLength(nums=[20, 1, 15, 3, 10, 5, 8]))
