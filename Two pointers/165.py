from typing import List, Tuple


class Solution1:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Time O(n + m + max(n, m))
        Space O(n + m + max(n, m))
        先把每个string split开，然后双指针遍历分开的数组，注意提取string变成int的时候会用到额外的空间。详细见注释。
        """
        # 转化成数组遍历
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            # 如果走到底了，直接赋值0，否则转化成int
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            # 如果两个数不相等，说明有version的区别
            if i1 != i2:
                # 返回结果1，和-1
                return 1 if i1 > i2 else -1

        # The versions are equal
        return 0


class Solution2:
    def get_next_chunk(self, version: str, n: int, p: int) -> Tuple[int, int]:
        # If pointer is set to the end of the string, return 0
        if p > n - 1:
            return 0, p

        # Find the end of the chunk
        p_end = p
        while p_end < n and version[p_end] != ".":
            p_end += 1

        # Retrieve the chunk
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])

        # Find the beginning of the next chunk
        p = p_end + 1

        return i, p

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Time O(max(n, m))
        Space O(max(n, m))
        我们可以一边找chunk一遍对比，不需要先split开。通过找下一个分隔符号来达到找chunk的方法。
        """
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        # Compare versions
        while p1 < n1 or p2 < n2:
            # 拿到下一个chunk的数字和起始位置
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)
            # 开始对比
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # The versions are equal
        return 0


s = Solution2()
print(s.compareVersion(version1="1.2", version2="1.10"))
print(s.compareVersion(version1="1.01", version2="1.001"))
print(s.compareVersion(version1="1.0", version2="1.0.0.0"))
