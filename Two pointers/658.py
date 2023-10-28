from typing import List


class Solution1:
    def left_bound(self, arr, target):
        # 找目标值左边界的标准写法
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1

        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time O(log(n) + n)
        Space O(n)
        二分法找到左边界，左边界表示大于目标值的最小数值。之后开始从左边界向两边扩散，依次添加进最终结果。
        这里添加的时候需要仔细判断离目标值的距离。此做法是左边每次都用insert来加入最终结果，不过insert操作是O(n)在数组内，
        并没有解法二里面直接分左右数组记录结果，然后sorted一下左边在拼接起来整个结果快。
        """
        # 二分搜索找到 x 的位置，或者左边界位置
        left_index = self.left_bound(arr, x)

        res = []
        # 两边都是开区间的写法 (left, right)
        left = left_index - 1
        right = left_index

        while k > 0:
            # 左右都有空间，则判断加入左或者右
            if left >= 0 and right <= len(arr) - 1 and k > 0:
                # 左边距离更小
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    # 左边因为是倒着添加，需要用insert到结果数组开头
                    res.insert(0, arr[left])
                    left -= 1
                    k -= 1
                else:
                    # 反之直接尾巴添加右边
                    res.append(arr[right])
                    right += 1
                    k -= 1
            # 左边有数，右边没有，直接加左边
            elif left >= 0 and k > 0:
                res.insert(0, arr[left])
                left -= 1
                k -= 1
            # 反之直接一直加右边
            elif right <= len(arr) - 1 and k > 0:
                res.append(arr[right])
                right += 1
                k -= 1

        return res


class Solution2:
    def left_bound(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1

        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time O(log(n) + n)
        Space O(n)
        思路完全同第一种，区别在于最终结果数组的构建，这里采用左右分别构建然后sorted左边后，拼接左右结果数组一起构成最终数组。
        """
        left_index = self.left_bound(arr, x)

        left_res = []
        right_res = []

        left = left_index - 1
        right = left_index

        while k > 0:
            if left >= 0 and right <= len(arr) - 1 and k > 0:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    # 所有逻辑同上，区别是这里不用insert，直接先添加，后边sort
                    left_res.append(arr[left])
                    left -= 1
                    k -= 1
                else:
                    right_res.append(arr[right])
                    right += 1
                    k -= 1
            elif left >= 0 and k > 0:
                left_res.append(arr[left])
                left -= 1
                k -= 1
            elif right <= len(arr) - 1 and k > 0:
                right_res.append(arr[right])
                right += 1
                k -= 1
        # 在这里sort左数组，因为添加的时候是倒序，insert是O(n)的操作，有时候这样最终sort反而更快，
        # 因为当极端情况只有左边的时候，O(n * n) > O(n * log(n))
        res = sorted(left_res) + right_res

        return res


s = Solution2()
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
print(s.findClosestElements(arr=[0, 1, 1, 1, 2, 3, 6, 7, 8, 9], k=9, x=4))
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
print(s.findClosestElements(arr=[0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))
