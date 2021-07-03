class Solution:
    def checkSubarraySum(self, nums: [int], k: int) -> bool:
        """
        前缀和思路，利用除法的余数来判断这段区间内加进来的数字是不是k的倍数，因为余数相同时说明这段区间内加进来的是k的倍数
        :param nums:
        :param k:
        :return:
        """
        m = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]

            if k == 0:
                key = total
            else:
                key = total % k

            if key in m:
                if i - m[key] >= 2:
                    return True
                continue    # 保存最小index，当已经存在时则不用再次存入，不然会更新索引值
            m[key] = i      # 储存的是余数对应的index

        return False

