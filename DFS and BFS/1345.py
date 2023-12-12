from collections import defaultdict
from typing import List


class Solution:
    def bfs(self, graph, arr):
        # 初始化列队，起点，存储当前(当前节点，走到此节点的step)
        queue = [(0, 0)]
        # 记录访问过的节点避免重复访问
        visited = set()
        visited.add(0)
        n = len(arr)

        while queue:
            # 当前节点
            index, step = queue.pop(0)
            # 走到重点，直接返回当前步数
            if index == n - 1:
                return step
            # 访问所有同一个数值的节点
            for nei in graph[arr[index]]:
                # 确保没有访问过
                if nei not in visited:
                    queue.append((nei, step + 1))
                    visited.add(nei)

            # 访问所有同一个数值的节点后清除此数值访问过的所有其它节点，及清除value，因为访问过一次就已添加过所有等值的节点
            graph[arr[index]].clear()

            # 访问前后节点
            for nei in [index - 1, index + 1]:
                # 前后节点在范围内并且没有访问过
                if 0 <= nei < n and nei not in visited:
                    queue.append((nei, step + 1))
                    visited.add(nei)

        return -1

    def minJumps(self, arr: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        构建graph，用BFS的思路找到最短的距离走到终点。这里构建graph比较trick。graph表示的只是当前数字可以去到所有同一个数字的index。
        我们遍历的时候是从节点index开始遍历，每个节点可以走到和它等值的index和前后index，分别加入列队继续下一步遍历。这里需要每次遍历完等值
        的节点的时候释放graph空间，也就是删除此数值对应的所有节点，这样下一次遍历到同一个数值的时候并不需要再去check一遍所有等值的节点是否
        访问过，大大节省了如果整个graph都是同一个数值的特殊情况。
        """
        graph = defaultdict(list)
        # 构建graph，数值 -> [index1, index2]
        for i in range(len(arr)):
            graph[arr[i]].append(i)

        res = self.bfs(graph, arr)

        return res


s = Solution()
print(s.minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
print(s.minJumps(arr=[7]))
print(s.minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]))
