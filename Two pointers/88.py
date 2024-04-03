from typing import List


class Solution1:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Time O(n + m)
        Space O(1)
        三指针倒叙思想，数组的倒叙遍历一定要熟记，
        """
        # while n > 0 and m > 0:
        #     if nums1[m - 1] <= nums2[n - 1]:
        #         nums1[m - 1 + n] = nums2[n - 1]
        #         # m -= 1
        #         n -= 1
        #     else:
        #         nums1[m - 1 + n] = nums1[m - 1]
        #         m -= 1
        #
        # while n > 0:
        #     nums1[m - 1 + n] = nums2[n - 1]
        #     n -= 1

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


class Solution2:
    def partition(self, arr: List[int], left: int, right: int) -> int:
        # 随机选择一个作为pivot指针，这里也可以用random.randint(left, right)
        pivot = left

        # 先把pivot指针对应的数放到最右边去
        arr[pivot], arr[right] = arr[right], arr[pivot]

        # store 指针用来找到大于pivot指针对应数的index
        store_index = left
        # 遍历数组
        for i in range(left, right):
            # 如果当前数字小于最右边的数字，也就是pivot指针数字
            if arr[i] <= arr[right]:
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

    def sort(self, nums):
        left = 0
        right = len(nums) - 1
        self.quick_sort(nums, left, right)

        return nums

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Time O((n + m) * log(n + m))
        Space O(1)
        合并之后，进行in-palace的快排序
        """
        nums1[m:] = nums2

        self.sort(nums1)

        return nums1


class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Time O(n + m)
        Space O(1)
        从后往前进行拉链式三指针排序，和思路1一样只是写法不一样
        """
        # 两个指针分别初始化在两个数组的最后一个元素（类似拉链两端的锯齿）
        p1 = m - 1
        p2 = n - 1
        # 生成排序的结果（类似拉链的拉锁）
        p = len(nums1) - 1

        # 从后向前生成结果数组，类似合并两个有序链表的逻辑
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 可能其中一个数组的指针走到尽头了，而另一个还没走完
        # 因为我们本身就是在往 nums1 中放元素，所以只需考虑 nums2 是否剩元素即可
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

        return nums1


s = Solution3()
print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
