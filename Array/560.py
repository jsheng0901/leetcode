class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        """
        time O(n), space O(n)
        每次记录前缀和，check pre_sum - k 是否出现过，如果出现过，意味着之前有前缀和等于rest，
        因为pre_sum1 - pre_sum2 = k 及为我们要找的区间sub-array
        :param nums:
        :param k:
        :return:
        """
        map = {0: 1}
        count = 0
        pre_sum = 0
        for i in nums:
            pre_sum += i
            if pre_sum - k in map:
                count += map[pre_sum - k]

            if pre_sum in map:
                map[pre_sum] += 1
            else:
                map[pre_sum] = 1

        return count


s = Solution()
print(s.subarraySum(nums=[1, 1, 1], k=2))
