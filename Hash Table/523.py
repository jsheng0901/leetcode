from typing import List


class Solution:
    def checkSubarraySum(self, nums: [int], k: int) -> bool:
        """
        Time O(n)
        Space O(n)
        前缀和思路，利用除法的余数来判断这段区间内加进来的数字是不是k的倍数，因为余数相同时说明这段区间内加进来的是k的倍数。
        """
        # 记录余数和index的关系，用来判断子串长度
        m = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            # 特殊情况 k = 0 的时候，直接等于total
            if k == 0:
                key = total
            else:
                key = total % k

            if key in m:
                if i - m[key] >= 2:
                    return True
                continue  # 保存最小index，当已经存在时则不用再次存入，不然会更新索引值
            m[key] = i  # 储存的是余数对应的index

        return False


class Solution2:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Time O(n)
        Space O(n)
        一样的思路，不一样的写法，不用特殊照顾0的情况，余数判断加进来的0一定是被整除的。
        """
        rest_to_index = {0: -1}
        pre_sum = 0

        for i in range(len(nums)):
            pre_sum += nums[i]
            # 如果存在，不用更新index，保存最小index
            if pre_sum % k in rest_to_index:
                rest_index = rest_to_index[pre_sum % k]
                if i - rest_index >= 2:
                    return True
            # 不存在则更新index
            else:
                rest_to_index[pre_sum % k] = i

        return False


s = Solution2()
print(s.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
print(s.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
print(s.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
