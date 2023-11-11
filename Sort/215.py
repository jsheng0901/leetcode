import heapq
import random
from typing import List


class Solution1:
    def select(self, left, right, k, nums):
        if left == right:
            return nums[left]

        # select a random pivot_index between
        pivot_index = left

        # find the pivot position in a sorted list
        pivot_index = self.partition(left, right, pivot_index, nums)

        # the pivot is in its final sorted position
        if k == pivot_index:
            return nums[k]
        # go left
        elif k < pivot_index:
            return self.select(left, pivot_index - 1, k, nums)
        # go right
        else:
            return self.select(pivot_index + 1, right, k, nums)

    def partition(self, left, right, pivot_index, nums):
        pivot = nums[pivot_index]

        # 1. move pivot to end, to make sure all
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def findKthLargest(self, nums: [int], k: int) -> int:
        """
        Time O(n)
        Space O(1)
        1. 在数组区间随机取 pivot index = left + random[right-left] .
        2. 根据pivot 做 partition，在数组区间，把小于pivot的数都移到pivot左边。
        3. 得到pivot的位置 index，compare(index, (n-k)).
            a. index == n-k -> 找到第`k`大元素，直接返回结果。
            b. index < n-k -> 说明在`index`右边，继续找数组区间`[index+1, right]`
            c. index > n-k -> 那么第`k`大数在`index`左边，继续查找数组区间`[left, index-1]`.
        """

        return self.select(0, len(nums) - 1, len(nums) - k, nums)


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time O(nlog(k))
        Space O(k)
        n次操作，每次删除和添加都log(k)，小顶堆的操作和堆内元素个数有关系。采用小顶堆，维持k个元素在堆内，最后堆顶元素及第k个最大的元素。
        """
        # 小顶堆，堆顶是最小元素
        pq = []
        for num in nums:
            # 每个元素都要过一遍二叉堆
            heapq.heappush(pq, num)
            # 堆中元素多于 k 个时，删除堆顶元素
            if len(pq) > k:
                heapq.heappop(pq)
        # pq 中剩下的是 nums 中 k 个最大元素，
        # 堆顶是最小的那个，即第 k 个最大元素
        return pq[0]


class Solution3:
    def quick_select(self, nums, k):
        # 随机选取pivot
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        # 小于pivot放左边，大于放右边，等于放中间
        for num in nums:
            if num > pivot:
                right.append(num)
            elif num < pivot:
                left.append(num)
            else:
                mid.append(num)

        # 如果k小于左边，说明在左侧，等价于二叉树的左子树，继续递归遍历左子树
        if k <= len(left):
            return self.quick_select(left, k)

        # 同上，继续递归遍历右子树
        if len(left) + len(mid) < k:
            return self.quick_select(right, k - len(left) - len(mid))

        # 找到最终数组只有一个数的时候，也就是我们要找的数，及叶子结点
        return pivot

    def findKthLargest(self, nums, k):
        """
        Time O(n)
        Space O(n)
        同第一种方法，快排序的逻辑，随机选择一个pivot，小于它的放左边，大于它的放右边，如果k小于左边的长度，说明在左边，
        大于左边+中间，说明在右边，继续递归直到找到pivot只有一个数字的时候在数组里面，此数字就是我们要找的第k个最小的数字，
        这里k需要转换一下，因为题目说的是找第k个最大的数字，等价于找len(nums) - k + 1最小的数字。
        快排及二叉树的前序遍历，当前节点处理构建节点的左右子树，找到合理的方向后，遍历左子树或者右子树。
        走到叶子节点及找到结果，之后回溯返回到根节点。
        """

        return self.quick_select(nums, len(nums) - k + 1)


s = Solution3()
print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
