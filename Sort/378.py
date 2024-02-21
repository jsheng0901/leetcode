import heapq
from typing import List


class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time O(n^2 * log(n^2))
        Space O(n^2)
        直接合并所有list，然后整体sort然后返回相对应的index，这里的n表示宽度
        """
        matrix_reshape = []
        for row in matrix:
            matrix_reshape += row

        matrix_reshape.sort()

        return matrix_reshape[k - 1]


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time O(n^2 * log(n^2) + k * log(n^2))
        Space O(n^2)
        对每一个元素进行插入小顶堆，之后再弹出k个最小值从小顶堆，最后一个弹出的就是结果。太多的空间和时间浪费了，因为我们并不需要存储和loop
        所有元素进小顶堆。
        """
        matrix_pq = []
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                heapq.heappush(matrix_pq, matrix[i][j])

        while k > 0:
            top = heapq.heappop(matrix_pq)
            k -= 1

        return top


class Solution3:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time O( min(k, n) + k * log(min(k, n)) )
        Space O(min(k, n))
        这道题类似23题合并K个升序链表的变体。
        矩阵中的每一行都是排好序的，就好比多条有序链表，用优先级队列施展合并多条有序链表的逻辑就能找到第 k 小的元素了。
        先存储min(k, n)个最小元素，下一个就是弹出的最小元素的下一列的元素入列队。之后继续弹出直到k个元素找到。
        """
        matrix_pq = []
        n = len(matrix)
        # 存储二元组 (matrix[i][j], i, j)
        # i, j 记录当前元素的索引位置，用于生成下一个节点，下一个节点一定是 i，j + 1
        # 初始化优先级队列，把每一行的第一个元素装进去
        for i in range(min(k, n)):
            heapq.heappush(matrix_pq, [matrix[i][0], i, 0])

        # 执行合并多个有序链表的逻辑，找到第 k 小的元素
        while matrix_pq and k > 0:
            # 当前最小元素的三个信息
            top = heapq.heappop(matrix_pq)
            res = top[0]
            i, j = top[1], top[2]
            k -= 1
            # 如果下一个节点存在，链表中的下一个节点加入优先级队列
            if j + 1 < n:
                heapq.heappush(matrix_pq, [matrix[i][j + 1], i, j + 1])

        return res


class Solution4:
    def count_less_equal(self, matrix, mid, smaller, larger, n):
        # 找有多少个数小于等于我们当前的虚拟中位数，这里我们只需要O(n)的时间复杂度进行搜索
        count = 0
        # 我们从左下角开始search
        row = n - 1
        col = 0

        # 当数字没有越界我们继续
        while row >= 0 and col < n:
            # 当前数字大于中位数，说明我们要向上移动，找下一个小一点的数，因为column也是有序的
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            # 当前数字小于中位数
            else:
                smaller = max(smaller, matrix[row][col])
                # 说明此时当前数字和此数字上面的数字都小于中位数，进行叠加count
                count += row + 1
                # 我们向右边移动，找下一个大一点的数
                col += 1

        return count, smaller, larger

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time O(n * log(max - min))  max - max number inf matrix, same as min
        Space O(1)
        当我们进行二分法搜索的时候我们需要知道index在有序的数列里面，但是这个题我们可以转化成在一个数字范围内我们搜索想要找到的第几个数。
        所以中位数不是通过media index计算得到的，是计算中位平均数得到的。这个数比一定真实存在matrix里面。之后我们判断小于这个数的左边部分
        在matrix里面有多少个数，之后就有三种情况
        1. 左边的size等于k，也就是说比我们虚拟的中位数小的最大的数就是我们要找的数
        2. 左边size小于k，此时我们应该更新左指针到大于我们虚拟的中位数的最小的数
        3. 左边size大于k，此时我们应该更新右指针到小于我们虚拟的中位数的最大的数
        """
        n = len(matrix)
        # 左指针和右指针，这里不是index是数值
        start, end = matrix[0][0], matrix[-1][-1]

        while start < end:
            # 中间数值
            mid = start + (end - start) / 2
            # 当前最大和最小的数，需要记录用于左右指针移动
            smaller, larger = matrix[0][0], matrix[-1][-1]

            count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger, n)
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:
                end = smaller

        return start


s = Solution3()
print(s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
