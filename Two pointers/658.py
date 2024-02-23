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
        Space O(n) -> O(1) output 不算的情况下
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
        Space O(n) -> O(1) output 不算的情况下
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


class Solution3:
    def left_bound(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                right = mid - 1

        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time O(log(n) + n)
        Space O(n) -> O(1) output 不算的情况下
        思路完全同第二种，区别在于最终结果数组的构建，这里并不需要最后sort一下，可以在叠加的时候就反过来顺序从头开始叠加。
        """
        left_index = self.left_bound(arr, x)

        left_res = []
        right_res = []

        left = left_index - 1
        right = left_index

        while k > 0:
            if left >= 0 and right <= len(arr) - 1 and k > 0:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    # 这里是主要不一样的地方，左边数组反向叠加
                    left_res = [arr[left]] + left_res
                    left -= 1
                    k -= 1
                else:
                    right_res.append(arr[right])
                    right += 1
                    k -= 1
            elif left >= 0 and k > 0:
                left_res = [arr[left]] + left_res
                left -= 1
                k -= 1
            elif right <= len(arr) - 1 and k > 0:
                right_res.append(arr[right])
                right += 1
                k -= 1

        # 不需要最后sort
        res = left_res + right_res

        return res


class Solution4:
    def left_bound(self, arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                right = mid - 1

        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time O(log(n) + n)
        Space O(n) -> O(1) output 不算的情况下
        思路完全同第二种，区别在于最终结果数组的构建，这里直接通过扩算区间的方式加入最终result。
        """
        # 二分搜索找到 x 的位置
        p = self.left_bound(arr, x)
        # 两端都开的区间 (left, right)
        left, right = p - 1, p
        res = []
        # 扩展区间，直到区间内包含 k 个元素
        while right - left - 1 < k:
            # 左边没有数了
            if left == -1:
                res.append(arr[right])
                right += 1
            # 右边没有数了
            elif right == len(arr):
                res.insert(0, arr[left])
                left -= 1
            # 右边更近
            elif x - arr[left] > arr[right] - x:
                res.append(arr[right])
                right += 1
            # 左边更近
            else:
                res.insert(0, arr[left])
                left -= 1

        return res


class Solution5:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Time O(log(n - k) + k) 搜索区间不需要包括k个数的区间。最后的k是因为构建output数组需要O(k)的时间去index。
        Space O(1)
        更巧妙的写法，既然可以找到左边界，那么我们可以直接找到最终区间的左边界，因为数组是递增的顺序。所以最终区间也是连续的一个子区间。
        这里核心难点是如何移动左右指针。因为我们找的是左边界，所以我们计算 arr[mid] 和arr[mid + k]到target值的距离，如果arr[mid]
        更近则移动右指针，反之移动左指针。
        """
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k

        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            # 如果 target 到 arr[mid + k] 的距离更近
            # 这里不需要绝对值，因为三种情况，
            # 1. arr[mid] 和 arr[mid + k] 都在x的左边，此时 x - arr[mid] 一定更大，也就是 arr[mid + k] 的距离更近
            # 2. arr[mid] 和 arr[mid + k] 都在x的右边，此时 arr[mid + k] - x 一定更大，也就是 arr[mid] 的距离更近
            # 3. x 在 arr[mid] 和 arr[mid + k] 的中间，此时 x - arr[mid] 更大的时候也就是 arr[mid + k] 的距离更近
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


s = Solution4()
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
print(s.findClosestElements(arr=[0, 1, 1, 1, 2, 3, 6, 7, 8, 9], k=9, x=4))
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
print(s.findClosestElements(arr=[0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))
