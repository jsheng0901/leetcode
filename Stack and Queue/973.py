from heapq import *


class Solution1(object):
    def kClosest(self, points, K):
        """
        直接排序 O(nlog(n))
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]


class Solution2(object):
    def kClosest(self, points, K):
        """
        最小堆，先算出所有距離，然後入堆，然後pop前k个, O(nlog(n))
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance = []

        for index, (i, j) in enumerate(points):
            heappush(distance, (i ** 2 + j ** 2, index))
        res = []
        while K:
            K -= 1
            _, idx = heappop(distance)
            res.append(points[idx])

        return res


class Solution3:
    def distance(self, points):
        return points[0] ** 2 + points[1] ** 2

    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        """loop points同时维护一个单调递增的stack，O(n^2) worst case, 超时过不了"""
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
            if d < pivot:
                points[store_index], points[i] = points[i], points[store_index]
                store_index += 1

        # 3. move pivot to its final place
        points[right], points[store_index] = points[store_index], points[right]

        return store_index

    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        """
        O(n) time, O(n) space
        快排，quicksort, 找到前k个最小的距离的点排在最前面，用partition的思路
        """
        return self.select(0, len(points) - 1, k - 1, points)


s = Solution4()
print(s.kClosest([[0, 1], [1, 0]], 2))
print(s.kClosest(points=[[1, 3], [-2, 2]], k=1))
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
