from typing import List
from collections import defaultdict, deque


class Solution:
    def get_diagonal(self, nums, x, y, n):
        res = []
        # 越界判断，这里会一直向斜上方判断，哪怕没有此cell，所以费时
        while x >= 0 and y < n:
            if y < len(nums[x]):
                res.append(nums[x][y])
            x -= 1
            y += 1

        return res

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Time O(n * m)
        Space O(1)
        思路直接，从左上到左下，从左下到右下，逐一遍历，但是因为此题有可能出现每一行的大小不一样的情况，所以最差的情况下，最后一行有n个元素，
        但是上面的全都是1个元素，此时越界的判断需要遍历整个nums，很多地方都是空的cell。所以很明显TLE。
        """
        m = len(nums)
        n = 0
        # 拿到最长的一行长度
        for num in nums:
            n = max(n, len(num))

        res = []
        # 遍历所有对角线的起点
        for i in range(m + n - 1):
            # 如果是最左边的起点
            if i < m:
                # 起始点位置
                start_x = i
                start_y = 0
                # 拿到此对角线的结果
                sub = self.get_diagonal(nums, start_x, start_y, m, n)
            # 如果是最下边的起点
            elif i >= m:
                # 起始点位置
                start_x = m - 1
                start_y = i - m + 1
                sub = self.get_diagonal(nums, start_x, start_y, m, n)
            # 叠加进结果
            res = res + sub

        return res


class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        所有的同一个对角线上cell的值都是等于 col + row。利用这一个特性，从下到上从左到右，遍历所有cell，
        记录他们的 row + col 值进一个dictionary，然后再从1的值作为key开始遍历dictionary，存储所有结果。
        """
        groups = defaultdict(list)
        # 从左到右，从上到下
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                # 对角线的值
                diagonal = row + col
                # 加入进dictionary
                groups[diagonal].append(nums[row][col])

        res = []
        curr = 0
        # 加入所有value值进结果
        while curr in groups:
            res.extend(groups[curr])
            curr += 1

        return res


class Solution3:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(sqrt(n))
        还是上面的思路，每个对角线到起始点(0, 0)的距离就是他们的对角线的值，同时也是从(0, 0)作为起点开始的BFS结果。
        这里注意先加入cell下面的值，再加入右边的值，保证了顺序，同时对于不是第一列的cell，只需要加入右边的值，
        下面的值已经在前一个对角线弹出列队的时候加入进了列队。同时也不需要visited数组记录是否会重复访问。
        """
        queue = deque([(0, 0)])
        ans = []

        while queue:
            # 当前cell
            row, col = queue.popleft()
            # 进入结果
            ans.append(nums[row][col])

            # 如果是第一列，先加入下面的cell值
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))

            # 再加入右边的cell值，保证了进入结果的顺序
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return ans


s = Solution3()
print(s.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
