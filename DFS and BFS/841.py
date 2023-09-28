from typing import List


class Solution1:
    def dfs(self, rooms, room, visited, path):

        # 这是另一种写法，进递归再判断当前节点
        # 本层递归是true，说明访问过，立刻返回
        # if visited[room]:
        #     return

        # 基本dfs框架，进入递归的一定是符合条件的，再下一层loop里面已经check过，
        # 这里就不需要写停止条件，因为能进入的一定合规，并且走到底后直接return

        # 记录访问过的房间进visited和path
        path.append(room)
        visited[room] = True

        # 访问此房间所有钥匙对应的房间
        for key in rooms[room]:
            # 如果没有访问过进入下一个房间
            # 处理下一层节点，判断是否要进行递归，不符合的不进递归
            if visited[key] is False:
                self.dfs(rooms, key, visited, path)

        # 回溯当前节点的位置
        # 但是本题是需要判断 0节点是否能到所有节点，那么我们就没有必要回溯去撤销操作了，只要遍历过的节点一律都标记上。

        return

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Time O(n)
        Space O(n)
        rooms就是有向图，我们从0开始dfs遍历整个图，如果都访问说明走过的path长度等于rooms房间个数，如果不相等说明有房间没办法访问。
        visited数组记录不要重复访问走过的房间。
        """
        visited = [False] * len(rooms)
        path = []

        self.dfs(rooms, 0, visited, path)

        return len(path) == len(rooms)


class Solution2:
    def dfs(self, rooms, room, visited):

        visited[room] = True
        for key in rooms[room]:
            if visited[key] is False:
                self.dfs(rooms, key, visited)

        return

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Time O(n)
        Space O(n)
        逻辑同上，区别在于直接visited数组记录是否访问过，最终check是否有false在visited里面。
        """
        visited = [False] * len(rooms)

        self.dfs(rooms, 0, visited)

        return all(visited)


s = Solution2()
print(s.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
print(s.canVisitAllRooms(rooms=[[1], [2], [3], []]))
