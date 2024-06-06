class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        Time O(n)
        Space O(n)
        把方向转化成数字，然后每次计算下一个位置，如果出现过则返回true，没出现过继续下一个方向，并记录访问过的点。
        """
        # 构建hashmap
        directions = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0)
        }

        # 起点
        start_x = 0
        start_y = 0
        # 起点加入访问记录
        visited = set()
        visited.add((0, 0))

        # 遍历每个方向
        for direction in path:
            step = directions[direction]
            # 下一个点的位置
            start_x += step[0]
            start_y += step[1]
            # 出现过，说明访问过，直接返回
            if (start_x, start_y) in visited:
                return True

            # 没出现过，加入访问过记录
            visited.add((start_x, start_y))

        return False


s = Solution()
print(s.isPathCrossing(path="NES"))
print(s.isPathCrossing(path="NESWW"))
