class Solution:
    """
    O(m*n) time, O(m*n) space, only need dfs, set compare takes O(1)
    we do the dfs store all island relative position into set, then every time add frozenset into set to compare
    """
    def numDistinctIslands(self, grid: [[int]]) -> int:
        # this compare unique function is too slow, used set add set (frozenset)
        # def current_island_is_unique():
        #     for other_island in unique_islands:
        #         if len(other_island) != len(current_island):
        #             continue
        #         for cell_1, cell_2 in zip(current_island, other_island):
        #             if cell_1 != cell_2:
        #                 break
        #         else:
        #             return False
        #     return True

        # Do a DFS to find all cells in the current island.
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or grid[row][col] == 0:
                return
            seen.add((row, col))
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Repeatedly start DFS's as long as there are islands remaining.
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    current_island = set()
                    row_origin = row
                    col_origin = col
                    dfs(row, col)
                    if current_island:
                        unique_islands.add(frozenset(current_island))
        return len(unique_islands)


