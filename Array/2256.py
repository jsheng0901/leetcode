from typing import List


class Solution1:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        频繁对一个区域进行计算，明显是前缀和的题型。构建前缀和，然后遍历所有index，分别计算每个index对应的题目要求的average，找最小的index。
        此题有两个trick的地方，第一个是average要求整数，所以要round到int。第二个是difference是绝对值，也就是说一旦我们找到difference
        为0的index的时候，就可以结束遍历了，不需要继续进行下去，因为一定是最小值。详细见注释。
        """
        n = len(nums)
        min_diff = float('inf')
        res = 0
        pre_sum = [0] * (len(nums) + 1)
        # 计算前缀和数组的标准写法
        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            # 计算前半部分
            first = pre_sum[i + 1] // (i + 1)
            # 计算后半部分，这里需要注意的是，如果是最后一个index，第二部分一定是0，不需要再计算，不然会遇到除以0的情况
            if i == len(nums) - 1:
                second = 0
            else:
                second = (pre_sum[n] - pre_sum[i + 1]) // (n - i - 1)
            diff = abs(first - second)
            # trick的地方，找到0后就不用再遍历了，因为一定是最小difference对应的index
            if diff == 0:
                res = i
                break
            # 更新最小difference对应的index
            if diff < min_diff:
                min_diff = diff
                res = i

        return res


class Solution2:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        一模一样的思路，但是空间可以优化成O(1)，我们并不需要记录所有前缀和进数组，计算总和之后，每次遍历index的时候同时计算当前前缀和，用一个
        参数时刻更新记录当前前缀和即可。详细见注释。
        """
        n = len(nums)
        min_diff = float('inf')
        res = 0
        pre_sum = 0
        # 计算总和，也可以写个loop算，一样的逻辑
        total_sum = sum(nums)

        for i in range(len(nums)):
            # 更新当前前缀和
            pre_sum += nums[i]
            first = pre_sum // (i + 1)
            if i == len(nums) - 1:
                second = 0
            else:
                second = (total_sum - pre_sum) // (n - i - 1)
            diff = abs(first - second)
            # trick的地方，找到0后就不用再遍历了，因为一定是最小difference对应的index
            if diff == 0:
                res = i
                break
            if diff < min_diff:
                min_diff = diff
                res = i

        return res


s = Solution2()
print(s.minimumAverageDifference(nums=[2, 5, 3, 9, 5, 3]))
print(s.minimumAverageDifference(nums=[0, 1, 0, 1, 0, 1]))
