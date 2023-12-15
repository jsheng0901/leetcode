import heapq
from typing import List


class Solution1(object):
    def kClosest(self, points, K):
        """
        Time O(n * log(n))
        Space O(1)
        直接排序，此方案最快。
        """
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]


class Solution2(object):
    def kClosest(self, points, K):
        """
        Time O(n * log(n))
        Space O(n * log(n))
        最小堆，先算出所有距离，然後入堆，然後pop前k个
        """
        distance = []

        for index, (i, j) in enumerate(points):
            heapq.heappush(distance, (i ** 2 + j ** 2, index))

        res = []
        while K:
            K -= 1
            _, idx = heapq.heappop(distance)
            res.append(points[idx])

        return res


class Solution3:
    def distance(self, points):
        return points[0] ** 2 + points[1] ** 2

    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        """
        Time O(n^2)
        Space O(n)
        loop points同时维护一个单调递增的stack， 超时过不了
        """
        stack1 = []
        stack2 = []

        for i in range(len(points)):
            d = self.distance(points[i])
            if len(stack1) == 0:
                stack1.append((d, i))
            elif 0 < len(stack1) < k and stack1[-1][0] <= d:
                stack1.append((d, i))
            elif stack1[-1][0] > d:
                while len(stack1) > 0 and stack1[-1][0] > d:
                    stack2.append(stack1.pop())

                stack1.append((d, i))
                while len(stack1) < k and len(stack2) > 0:
                    stack1.append(stack2.pop())

        return [points[i[1]] for i in stack1]


class Solution4:
    def select(self, left, right, k, points):
        # select a random pivot_index between
        pivot_index = left

        # find the pivot position in a sorted list
        pivot_index = self.partition(left, right, pivot_index, points)

        # the pivot is in its final sorted position
        if k == pivot_index:
            return points[:k + 1]
        # go left
        elif k < pivot_index:
            return self.select(left, pivot_index - 1, k, points)
        # go right
        else:
            return self.select(pivot_index + 1, right, k, points)

    def partition(self, left, right, pivot_index, points):
        pivot = points[pivot_index][0] ** 2 + points[pivot_index][1] ** 2

        # 1. move pivot to end, to make sure all
        points[pivot_index], points[right] = points[right], points[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            d = points[i][0] ** 2 + points[i][1] ** 2
            # 这里很trick的是一定要写等于，相当于所有小于等于的点都放到左边去，例子: [[10000, 10000], ...] k = 10000
            # test case里面有一种情况，10000个点全都是一模一样的距离，不写等于的话相当于每个点永远没有小于自己的点的情况，
            # 则此时每个点的store index永远是input进来的left，也就是说我们需要遍历所有点每个点计算一遍所有点的距离，
            # 此时时间复杂度是O(n^2)，改成小于等于后直接第一个点的store index就是最右边，之后判断k == pivot_index，O(n)时间直接返回。
            if d <= pivot:
                points[store_index], points[i] = points[i], points[store_index]
                store_index += 1

        # 3. move pivot to its final place
        points[right], points[store_index] = points[store_index], points[right]

        return store_index

    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        """
        Time O(n)
        Space O(1)
        快排，quicksort, 找到前k个最小的距离的点排在最前面，用partition的思路。这里有个test case的特殊情况，详细见注释。
        """
        return self.select(0, len(points) - 1, k - 1, points)


class Solution5:
    def distance(self, x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time O(n * log(n))
        Space O(k * log(k))
        大顶堆，一直维护一个k大小的长度的优先列队大顶堆，对比小顶堆虽然都需要遍历一次所有点，但是空间维护不需要存储所有坐标。
        """
        pq = []

        for i in range(len(points)):
            point = points[i]
            dist = self.distance(point[0], point[1])
            # 维护大顶堆
            heapq.heappush(pq, (-dist, i))
            # 长度超出则弹出栈顶更大的那个
            if len(pq) > k:
                heapq.heappop(pq)

        # 最后剩下的一定是最小的k个，直接全部弹出加入结果
        res = []
        while pq:
            _, i = heapq.heappop(pq)
            res.append(points[i])

        return res


s = Solution5()
print(s.kClosest([[0, 1], [1, 0]], 2))
print(s.kClosest(points=[[1, 3], [-2, 2]], k=1))
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
print(s.kClosest(points=[[1, 3], [-2, 2]], k=1))
