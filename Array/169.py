from collections import Counter
from typing import List


class Solution1:
    def majorityElement(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(1)
        majority vote算法。因为一定会有众数出现，所以我们可以假设众数是正，其它是负。见注释。
        """
        # 我们想寻找的那个众数
        target = 0
        # 计数器（类比带电粒子例子中的带电性）
        count = 0
        for i in range(len(nums)):
            if count == 0:
                # 当计数器为 0 时，假设 nums[i] 就是众数
                target = nums[i]
                # 众数出现了一次
                count = 1
            elif nums[i] == target:
                # 如果遇到的是目标众数，计数器累加
                count += 1
            else:
                # 如果遇到的不是目标众数，计数器递减
                count -= 1
        # 回想带电粒子的例子
        # 此时的 count 必然大于 0，此时的 target 必然就是目标众数
        return target


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        hash table的标准写法，统计所有出现的频率然后找到频率的最大值元素。
        """
        freq = Counter(nums)

        major_freq = float('-inf')
        major_el = nums[0]
        for k, v in freq.items():
            if v > major_freq:
                major_freq = v
                major_el = k

        return major_el


s = Solution1()
print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
