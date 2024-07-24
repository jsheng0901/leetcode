from random import randint
from typing import List


class Solution1:

    def partition(self, arr: List[int], left: int, right: int) -> int:
        # 随机选择一个作为pivot指针，这里也可以用random.randint(left, right)
        pivot = randint(left, right)

        # 先把pivot指针对应的数放到最右边去
        arr[pivot], arr[right] = arr[right], arr[pivot]

        # store 指针用来找到大于pivot指针对应数的index
        store_index = left
        # 遍历数组
        for i in range(left, right):
            # 如果当前数字小于最右边的数字，也就是pivot指针数字
            if arr[i] < arr[right]:
                # 交换 store 指针对应的大于pivot指针的数字和当前数字，也就是把小于pivot的都移动到最右边去
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        # 最后store指针的位置就是当我们移动完所有小于pivot指针数字之后的下一个index也就是pivot应该移动回来的index
        arr[store_index], arr[right] = arr[right], arr[store_index]

        # 返回pivot指针数字排序完成后的index
        return store_index

    def quick_sort(self, arr: List[int], left: int, right: int) -> None:
        # 如果越界说明数组已经遍历结束
        if left >= right:
            return

        # 得到当前pivot指针排序完成后的位置，可以理解为树结构中的中间节点
        pivot = self.partition(arr, left, right)

        # 分别遍历pivot两边的数组，也就是树节点的左右子节点
        self.quick_sort(arr, left, pivot - 1)
        self.quick_sort(arr, pivot + 1, right)

    def sortArray(self, nums: [int]) -> [int]:
        """
        Time O(n * log(n))  worst case O(n^2)
        Space O(log(n))
        快速排序，这里会遇到worse case 所有数字都一样的情况，此时会变成O(n^2)的时间复杂度。会TLE。
        """
        self.quick_sort(nums, 0, len(nums) - 1)

        return nums


class Solution2:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # 合并后的数组
        result = []
        while left and right:
            # 对比两个数组的第一个元素
            # 小的数字弹出并放进去结果数组
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 如果左边还有数字，一定是有序的直接加到结果后面
        if left:
            result.extend(left)
        # 同理右边
        if right:
            result.extend(right)

        return result

    def sort(self, arr: List[int]) -> List[int]:
        # 走到底，只有一个元素，直接返回
        if len(arr) < 2:
            return arr
        # 找中间节点
        middle = len(arr) // 2
        # 左右递归，拿到合并成功的数组
        left = self.sort(arr[: middle])
        right = self.sort(arr[middle:])
        # 合并当前节点的左右子树数组
        sub_res = self.merge(left, right)

        return sub_res

    def sortArray(self, nums: [int]) -> [int]:
        """
        Time O(n * log(n))  worst case O(n * log(n))
        Space O(n)
        归并排序，worse case下也是就一样的速度 O(n * log(n))所以不会TLE。
        """
        return self.sort(nums)


class Solution3:
    def build_max_heap(self, arr: List[int]) -> None:
        length = len(arr)
        # 对每个节点构建大顶堆，除叶子结点
        for i in range(length // 2 - 1, -1, -1):
            self.heapify(arr, length, i)

    def heapify(self, arr: List[int], n: int, i: int) -> None:
        # 构建大顶堆算法
        # 初始化当前root index为最大值对应的index
        largest = i
        # 左右孩子节点的index
        left = 2 * i + 1
        right = 2 * i + 2

        # 如果左孩子更大，最大值对应的index赋值为左孩子
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 如果右孩子更大，最大值对应的index赋值为右孩子
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 如果当前root不是最大值对应的index，说明要进行swap，保证堆顶是最大值
        if largest != i:
            # swap两个index
            arr[i], arr[largest] = arr[largest], arr[i]
            # 继续递归原先最大值对于的index为root的子树
            self.heapify(arr, n, largest)

        return

    def sort(self, arr: List[int]) -> List[int]:
        # 初始化构建大顶堆，第一步
        self.build_max_heap(arr)

        # 从后向前重新构建大顶堆，每次堆缩小一个数
        for i in range(len(arr) - 1, -1, -1):
            # 把堆顶最大值放到最后一位去
            arr[0], arr[i] = arr[i], arr[0]
            # 对剩下的堆继续重新调整大顶堆，保证堆顶是最大值
            self.heapify(arr, i, 0)

        return arr

    def sortArray(self, nums: [int]) -> [int]:
        """
        Time O(n * log(n))
        Space O(log(n))
        堆排序，很稳定，任何情况都是一样的速度，不会TLE，比merge sort还快一些其实，不需要额外的数组空间来重组数组。
        """
        return self.sort(nums)


s = Solution3()
print(s.sortArray(nums=[5, 1, 1, 2, 0, 0]))
