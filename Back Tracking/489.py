class Solution:
    def cleanRoom(self, robot):
        """
        Time O(m)
        Space O(m)
        此题很巧妙，让机器人顺时针的方向走是此题的DFS方向。同时走到底的时候需要回溯回来，并且记录clean过的cell，
        这里直接把起始点当做 (0, 0) 记录访问过的cell。
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            # 当前cell记录访问过
            visited.add(cell)
            # 清理cell
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                # 这里的方向一定要维持顺时针的方向，所以需要引入余数，来保证永远是向右转。
                # 比如当前方向是向左，d=3，顺时针的方向应该是: 3(left), 0(up), 1(right), 2(down)
                # 当i等于1的时候，我们得到的是4，然而应该是0，应该是向右转也就是up这个方向，也就没有这
                # 所以引入余数在这里可以保证方向永远是落在 0, 1, 2, 3 这个范围内
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0],
                            cell[1] + directions[new_d][1])

                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    # 回溯
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        # 这里也要保证方向的顺序
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
