class Solution:
    def findCircleNum(self, isConnected: [[int]]) -> int:
        """
        O(n^2) time, O(n) space
        loop through all node, for each node, find all connected node and mark as visited, then keep loop next node
        used visited array to make sure if node is connected and seen before
        """
        def dfs(node):
            visited[node] = True
            for j in range(len(isConnected)):
                if isConnected[node][j] == 1 and node != j and visited[j] is False:
                    dfs(j)

            return

        res = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if visited[i] is False:
                res += 1
                dfs(i)

        return res


s = Solution()
# print(s.findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(s.findCircleNum(isConnected=[[1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0],
[0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1]]))
