class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        三指针倒叙思想，数组的倒叙遍历一定要熟记，
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[cur] = nums2[n - 1]
                n -= 1
            else:
                nums1[cur] = nums1[m - 1]
                m -= 1
            cur -= 1

        while n > 0:
            nums1[cur] = nums2[n - 1]
            n -= 1
            cur -= 1

        return nums1
