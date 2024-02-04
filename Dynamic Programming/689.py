from typing import List


class Solution1:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time O(n^3)
        Space O(1)
        brute force，写法遍历所有组合找到最大的情况，需要三层loop嵌套。当然没办法过测试，有很多重复计算。
        """
        n = len(nums)
        pre_sum = [0]
        cur_sum = 0
        # 计算前缀和方便快速查找一个区间的和，注意这里要记录index为0的情况
        for i in range(n):
            cur_sum += nums[i]
            pre_sum.append(cur_sum)

        max_sum = float('-inf')
        res = []
        # 第一个区间的结束位置
        for end1 in range(k - 1, n - 2 * k):
            # 第一个区间的开始位置
            start1 = end1 - k + 1
            # 第二个区间的结束位置
            for end2 in range(end1 + k, n - k):
                # 第二个区间的开始位置
                start2 = end2 - k + 1
                # 第三个区间的结束位置
                for end3 in range(end2 + k, n):
                    # 第三个区间的开始位置
                    start3 = end3 - k + 1
                    # 计算这三个区间对应的k个长度的区间的总和
                    sub_sum = ((pre_sum[end1 + 1] - pre_sum[start1]) + (pre_sum[end2 + 1] - pre_sum[start2]) +
                               (pre_sum[end3 + 1] - pre_sum[start3]))
                    # 如果大于当前最大值，更新结果
                    if sub_sum > max_sum:
                        max_sum = sub_sum
                        res = [start1, start2, start3]

        return res


class Solution2:
    def dp(self, nums, k, index, used, memo):
        # 如果当前已经使用三个区间，说明我们已经走到底了，返回0和空list
        if used == 3:
            return 0, []
        # 如果当前index + 还没有使用过的次数 * k，也就是说当前节点已经不足以继续进行下去组合成3个我们想要的k个length的区间，直接返回空
        if len(nums) < (3 - used) * k + index:
            return 0, []
        # 出现过在备忘录内，直接返回结果
        if (index, used) in memo:
            return memo[(index, used)]
        # 第一种情况，选择当前index作为区间起点，则下一个index起点为 index + k
        take_curr_sum, take_curr_index = self.dp(nums, k, index + k, used + 1, memo)
        # 第二种情况，不选择当前index作为区间起点，则下一个index起点为 index + 1
        skip_curr_sum, skip_curr_index = self.dp(nums, k, index + 1, used, memo)

        # 计算当前index下的区间总和
        take_curr_sum += sum(nums[index: index + k])
        # 如果大于第二种情况
        if take_curr_sum >= skip_curr_sum:
            # 记录进备忘录，这里区间起始index等于当前index+返回来的之前的index
            memo[(index, used)] = (take_curr_sum, [index] + take_curr_index)
        else:
            # 记录进备忘录，这里区间起始index等于第二种情况返回来的之前的index
            memo[(index, used)] = (skip_curr_sum, skip_curr_index)

        return memo[(index, used)]

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time O(n * k)
        Space O(n * k)
        用DFS带备忘录的的写法也就是DP的做法，每次对当前index有两种情况，第一种是选择作为起始点，第二种是不选择及跳过这个点。
        两种情况分别为子节点的返回值，找到一条合理的path，通过返回值计算最大值和对应的index，详细见注释。
        """
        memo = {}

        _, max_sum_index = self.dp(nums, k, 0, 0, memo)

        return max_sum_index


class Solution3:
    def dp(self, nums, k, index, used, memo, pre_sum):
        if used == 3:
            return 0, []

        if len(nums) < (3 - used) * k + index:
            return 0, []

        if (index, used) in memo:
            return memo[(index, used)]

        take_curr_sum, take_curr_index = self.dp(nums, k, index + k, used + 1, memo, pre_sum)
        skip_curr_sum, skip_curr_index = self.dp(nums, k, index + 1, used, memo, pre_sum)

        take_curr_sum += pre_sum[index]
        if take_curr_sum >= skip_curr_sum:
            memo[(index, used)] = (take_curr_sum, [index] + take_curr_index)
        else:
            memo[(index, used)] = (skip_curr_sum, skip_curr_index)

        return memo[(index, used)]

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time O(n * k)
        Space O(n * k)
        同思路2，只是我们每次计算区间和的时候并不需要每次都sum一遍，这样很费时，一开始计算好前缀和，直接找对应的index。
        注意这里前缀和区别与普通的前缀和，记录的是当前节点到k个length的区间总和
        """
        memo = {}
        pre_sum = []
        for i in range(len(nums) - k + 1):
            pre_sum.append(sum(nums[i: i + k]))

        _, max_sum_index = self.dp(nums, k, 0, 0, memo, pre_sum)

        return max_sum_index


s = Solution3()
print(s.maxSumOfThreeSubarrays(nums=[1, 2, 1, 2, 6, 7, 5, 1], k=2))
