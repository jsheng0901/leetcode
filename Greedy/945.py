from typing import List


class Solution1:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        贪心思路，把局部相等的先变成不相等的，全局达到不相等。
        先sort一下，这样保证数据从小到大，可以两两对比，遇到一样的数，后面一个直接+1，操作次数 +1，然后继续对比，
        """
        res = 0
        # 从小打到sort
        nums.sort()

        for i in range(1, len(nums)):
            # 如果当前数和前一个相等
            if nums[i] <= nums[i - 1]:
                # 变成unique数是多少
                unique_num = nums[i - 1] + 1
                # 计算需要多少次operation
                res += unique_num - nums[i]
                # 重新赋值
                nums[i] = unique_num

        # 返回结果
        return res


class Solution2:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        Time O(n + max)  max --> max num in nums
        Space O(n + max)
        换个思路，每个元素要不一样，说明每个元素出现的频率为1或者0，构建每个元素出现的频率数组，
        然后遇到频率大于1的元素就直接加到下一个元素上，以此类推，统计operation次数。
        """
        res = 0
        n = len(nums)
        # 当前最大值
        max_val = max(nums)
        # 当前最大值就是全部变成unique后最多会多出来的元素，这里index是数本身
        freq = [0] * (n + max_val + 1)

        # 统计当前元素的频率，num[1] 代表1这个数出现在nums里面的频率
        for num in nums:
            freq[num] += 1

        for i in range(len(freq)):
            # 如果小于等于1，一定是unique的，不需要任何操作
            if freq[i] <= 1:
                continue

            # 计算变成unique需要多少次操作
            duplicate_num = freq[i] - 1
            # 下一个数频率叠加
            freq[i + 1] += duplicate_num
            # 当前数频率变成1
            freq[i] = 1
            # 累加操作次数进结果
            res += duplicate_num

        return res


s = Solution2()
print(s.minIncrementForUnique(nums=[1, 2, 2]))
print(s.minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))
