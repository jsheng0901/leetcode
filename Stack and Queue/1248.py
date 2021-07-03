class Solution:
    def numberOfSubarrays(self, nums: [int], k: int) -> int:
        """
        前缀和思路，这里变成奇数个数和，同前缀和找rest，用hash map保存奇数和为多少的出现频率，每次找rest在map里面是否出现过
        :param nums:
        :param k:
        :return:
        """
        odd_number = 0
        count = 0
        m = {0: 1}

        for x in nums:
            if x % 2 != 0:
                odd_number += 1

            if odd_number - k in m:     # 如果出现过，说明找到一个区间，满足k次的需求
                count += m[odd_number - k]

            if odd_number in m:         # 记录奇数和出现的频率
                m[odd_number] += 1
            else:
                m[odd_number] = 1

        return count
