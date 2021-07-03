class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        # 存放结果
        resutl = []

        record = set(nums1)

        for i in set(nums2):
            if i in record:
                resutl.append(i)

        return resutl


s = Solution()
print(s.intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
