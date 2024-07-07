import heapq
from typing import List


class Solution1:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        贪心思路为主，对于所有最大的gap我们用梯子，其它的用砖块，这样可以保证最大化梯子的作用。也就是说我们需要维护一个小顶堆，记录所有
        最大的gap，堆的大小就是梯子的个数，其余的gap用砖块填满，直到没有足够的砖块。详细见注释。
        """
        # 小顶堆初始化
        pq = []
        # 记录需要的砖块的个数
        bricks_jumps = 0
        for i in range(1, len(heights)):
            # 如果前一个大于等于后一个，直接跳过
            if heights[i - 1] >= heights[i]:
                continue
            # 否则需要砖块或者梯子
            else:
                # 计算需要砖块的个数
                diff = heights[i] - heights[i - 1]
                # 加入进小顶堆
                heapq.heappush(pq, diff)
                # 如果堆的大小大于梯子的个数，说明此时我们需要弹出最小的那个变成用砖块
                while len(pq) > ladders:
                    # 更新需要的砖块的个数
                    bricks_jumps += heapq.heappop(pq)
            # 如果大于我们拥有的砖块个数，直接返回最远可以达到的index，这里需要 -1，因为超过的需求的时候是下一个index
            if bricks_jumps > bricks:
                return i - 1

        # 如果都可以达到，说明走到最后一步，直接返回最后一个index
        return len(heights) - 1


class Solution2:
    def is_reachable(self, heights, bricks, ladders, building_index):
        # 判断是否可以达到当前给定的index，其实和小顶堆的思路是一样的，
        # 先存储所有台阶
        climbs = []
        for i in range(1, building_index + 1):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                climbs.append(diff)
        # 进行sort一下，来实现最小的先用砖块
        climbs.sort()
        bricks_remaining = bricks
        ladders_remaining = ladders
        # 遍历所有台阶
        for climb in climbs:
            # 如果有砖块先用砖块
            if climb <= bricks_remaining:
                bricks_remaining -= climb
            # 如果没有砖块了有梯子继续用梯子
            elif ladders_remaining >= 1:
                ladders_remaining -= 1
            # 如果都没有了但是还有台阶，说明不可能reach，直接返回false
            else:
                return False

        # 能走到最后说明可以reach，返回true
        return True

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Time O(n * log(n) * log(n))
        Space O(n)
        二分法思路，最远可以达到的index之后一定都是不可以到达的，之前都是可以到达的。所以这里可以用是否可以到达此index来进行判断我们需要往
        那个方向走，如果可以到达说明当前index或者之后的index是最远index，如果不能达到说明一定之后的都不能达到，指针往左边走。
        """
        left = 0
        right = len(heights) - 1
        # 二分法判断
        while left <= right:
            mid = left + (right - left) // 2
            # 如果可以达到
            if self.is_reachable(heights, bricks, ladders, mid):
                # 移动左指针
                left = mid + 1
            # 否则不能达到
            else:
                # 移动右指针
                right = mid - 1

        # 跳出二分法loop时候是right = left + 1，此时左指针已经是不能reach的index，所以返回右指针为最远index
        return right


class Solution3:
    def get_sorted_climbs(self, heights):
        # 拿到所有台阶的sort之后的数组
        sorted_climbs = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                # 区别在这，记录台阶高度和对应的index
                sorted_climbs.append((diff, i))

        sorted_climbs.sort(key=lambda x: x[0])
        return sorted_climbs

    def is_reachable(self, bricks, ladders, sorted_climbs, building_index):
        # 计算剩余的砖块和梯子个数
        bricks_remaining = bricks
        ladders_remaining = ladders
        for climb_entry in sorted_climbs:
            # 当前台阶高度和对应的index
            climb = climb_entry[0]
            index = climb_entry[1]
            # 如果在我们搜索的index之后，直接跳过
            if index > building_index:
                continue
            # 剩余部分和思路2一样
            if climb <= bricks_remaining:
                bricks_remaining -= climb
            elif ladders_remaining >= 1:
                ladders_remaining -= 1
            else:
                return False

        return True

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Time O(n * log(n) + n * log(n))
        Space O(n)
        和思路2一模一样，区别在于判断是否可以reach到指定的index，我们不需要每次都sort一遍，完全可以一次性拿到所有的台阶，直接从小打到sort
        一遍，区别在于我们要存储每个台阶对应的index，这样我们遍历是否可以reach的时候，如果当前台阶在我们reach的index之前进行记录，如果不再
        直接跳过。从而达到只需要sort一次。
        """
        # 拿到所有sort过后的台阶
        sorted_climbs = self.get_sorted_climbs(heights)

        left = 0
        right = len(heights) - 1
        # 二分法遍历和思路2一样
        while left <= right:
            mid = left + (right - left) // 2

            if self.is_reachable(bricks, ladders, sorted_climbs, mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


s = Solution3()
print(s.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
