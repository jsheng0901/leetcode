from heapq import heappop, heappush


class Solution:
    def maximumMinimumPath(self, grid: [[int]]) -> int:
        """
        O(m*n*log(m*n) time, O(m*n) space
        bfs search, every time record min path number and save as max heap then compare and keep search till end
        """
        m, n = len(grid), len(grid[0])
        pq = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1
        while pq:
            cur_path_min, cur_i, cur_j = heappop(pq)
            if cur_i == m - 1 and cur_j == n - 1:
                return -cur_path_min
            for d_i, d_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i, new_j = cur_i + d_i, cur_j + d_j
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != -1:
                    heappush(pq, (-min(grid[new_i][new_j], -cur_path_min), new_i, new_j))
                    grid[new_i][new_j] = -1


s = Solution()
print(s.maximumMinimumPath(
    grid=[[2, 0, 5, 2, 0], [2, 4, 4, 4, 3], [1, 5, 0, 0, 0], [5, 4, 4, 3, 1], [1, 3, 1, 5, 3]]
))
