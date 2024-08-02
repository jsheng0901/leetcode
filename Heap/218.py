from typing import List
from sortedcontainers import SortedList


class Solution1:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Time O(n^2)
        Space O(n)
        此题的核心是理解意思先，对于所有点，我们需要找到的是这个点对应的最大值也就是最高值。我们可以先sort一下整个buildings，从左到右
        一次扫描所有点，对于每个点找到在buildings里面的最大高度，如果和前一个最大高度不一样，则加入结果，否则继续遍历。
        """
        # Collect and sort the unique positions of all the edges.
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        # 'answer' for skyline key points
        answer = []

        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height.
            max_height = 0

            # Iterate over all the buildings:
            for left, right, height in buildings:
                # Update 'max_height' if necessary.
                if left <= position < right:
                    max_height = max(max_height, height)

            # If it's the first key point or the height changes,
            # we add [position, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([position, max_height])

        # Return 'answer' as the skyline.
        return answer


class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Time O(n * log(n))
        Space O(n)
        此类型题都有一个基本思路是，对于需要计算所有点的情况，可以线性扫描线，但一定要先sort。
        延续思路1，如果我们每次都需要知道最大值的高度，那么可以维护一个大顶堆，达到每次拿第一个元素就是最大值，不需要再次遍历整个数组找最大值。
        这里用有序数组来实现大顶堆，方便添加和移除，并确保证都是log(n)的操作速度。
        从左到右扫描坐标时：
            当扫描到建筑物的左边界时，说明必然存在一条向右延伸的边。此时将高度加入到优先队列中。
            当扫描到建筑物的右边界时，说明从之前的左边界延伸的边结束了，此时将高度从优先队列中移除。
        因为三条高度相同的线应该合并为一个，所以我们用 prev 来记录之前上一个矩形高度。
            如果当前矩形高度 curr 与之前矩形高度 prev 相同，则跳过。
            如果当前矩形高度 curr 与之前矩形高度 prev 不相同，则将其加入到答案数组中，并更新上一矩形高度 prev 的值。
        """
        ans = []

        # 预处理所有的点，为了方便排序，对于左端点，令高度为负；对于右端点令高度为正
        positions = []
        for left, right, height in buildings:
            # 对于某个横坐标而言，可能会同时出现多个点，应当按照如下规则进行处理：
            # 优先处理左端点，再处理右端点
            # 如果同样都是左端点，则按照高度「从大到小」进行处理（将高度增加到优先队列中）
            # 如果同样都是右端点，则按照高度「从小到大」进行处理（将高度从优先队列中删掉）
            positions.append((left, -height))
            positions.append((right, height))

        # 先按照横坐标进行排序
        # 如果横坐标相同，则按照左端点排序
        # 如果相同的左/右端点，则按照高度进行排序
        positions.sort()

        # 初始化一个0，是为了方便记录building高度为0的拐点
        prev = 0
        # 有序列表充当大顶堆
        pq = SortedList([prev])

        for point, height in positions:
            if height < 0:
                # 如果是左端点，说明存在一条往右延伸的可记录的边，将高度存入优先队列
                # 注意这里要取负数，因为左端点存储的时候存的是负数
                pq.add(-height)
            else:
                # 如果是右端点，说明这条边结束了，将当前高度从队列中移除
                pq.remove(height)

            # 取出最高高度，如果当前不与前一矩形“上边”延展而来的那些边重合，则可以被记录
            cur = pq[-1]
            if cur != prev:
                ans.append([point, cur])
                prev = cur

        return ans


s = Solution2()
print(s.getSkyline(buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(s.getSkyline(buildings=[[0, 2, 3], [2, 5, 3]]))
