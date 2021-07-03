class Solution:
    def subarraysDivByK(self, nums: [int], k: int) -> int:
        """
        同样的前缀和，需要记录的是前缀除以k的余数，因为当余数一致的时候说明中间区间就是k的倍数
        :param nums:
        :param k:
        :return:
        """
        m = {0: 1}
        count = 0
        pre_sum = 0

        for x in nums:
            pre_sum += x

            if pre_sum % k in m:
                count += m[pre_sum % k]
                m[pre_sum % k] += 1
            else:
                m[pre_sum % k] = 1

        return count