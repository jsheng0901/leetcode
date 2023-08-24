from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        """
        Time O(n）
        Space O(n)
        hash table的典型应用，额外空间存储数据出现频率
        """
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                record[nums[i]] += 1
            else:
                record[nums[i]] = 1

        for k, v in record.items():
            if v == 1:
                return k

    def singleNumber2(self, nums: List[int]) -> int:
        """
        Time O(n）
        Space O(1)
        用数学方法计算，记录X+Y，3X+Y，此时 Y = (X+Y) - (3X+Y - X+Y)/2
        """
        set_sum = 0
        all_sum = 0
        n_set = set()

        for n in nums:
            all_sum += n
            if n not in n_set:
                n_set.add(n)
                set_sum += n

        return set_sum - int((all_sum - set_sum) / 2)


s = Solution()
print(s.singleNumber1(nums=[2, 2, 3, 2]))
