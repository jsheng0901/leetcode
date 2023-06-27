class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        """
        time: O(n) n = len(nums1) + len(nums2)
        space: O(n) n = len(result)
        """
        # 存放结果
        result = []

        record = set(nums1)

        for i in set(nums2):
            if i in record:
                result.append(i)

        return result


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
