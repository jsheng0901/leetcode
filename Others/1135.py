class Solution:
    def minimumCost(self, n: int, connections: [[int]]) -> int:
        """
        O(n log(n)) time, sort and union find both use n * log(n), O(n) space for union find list store
        Union Find/DSU
        """

        def find(edge):
            while self.root[edge] != edge:      # 找root节点
                edge = self.root[edge]
            return edge                         # return root节点，root节点是当前index等于当前index对应的值的时候的节点

        def union(edge1, edge2):
            root1 = find(edge1)
            root2 = find(edge2)
            if root1 != root2:          # union两个没有连接但是共用root的节点
                self.root[root2] = root1        # 把root1节点赋给root2节点作为parent root2 --> root1

        def isConnected(edge1, edge2):
            return find(edge1) == find(edge2)

        def allConnected():
            cRoot = find(1)                         # get root of random number
            for r in range(1, len(self.root)):      # if all connected, then all number root should be same
                if cRoot != find(r):                # if one root is not same, then which means not all node connected
                    return False                    # just stop and return false
            return True

        self.root = [i for i in range(n + 1)]       # 构建union find list [0, 1, 2, 3]
        connections.sort(key=lambda x: x[2])        # sort by distance cause we only need min distance to add
        cost = 0
        for edge1, edge2, val in connections:
            if not isConnected(edge1, edge2):       # if not connected, then we connect node, if connected we keep loop
                union(edge1, edge2)                 # connect node
                cost += val                         # cost plus
        print(self.root)
        if allConnected():                          # check if all node is connected
            return cost
        else:
            return -1


s = Solution()
print(s.minimumCost(n=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
