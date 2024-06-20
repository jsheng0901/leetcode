from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(1)
        遍历第一个数，存储出现的频率，遍历第二个数，如果出现过并且出现的频率大于0，则进入结果，并且同时记得 -1，因为我们已经用了一次。
        如果没有出现过直接跳过。
        """
        freq = {}
        res = []

        # 记录第一个数每个数字出现的频率
        for i in nums1:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in nums2:
            # 如果出现过并且频率大于0
            if i in freq and freq[i] > 0:
                res.append(i)
                freq[i] -= 1

        return res


s = Solution()
print(s.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(s.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
