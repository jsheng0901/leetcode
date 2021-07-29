# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        """递归思路DFS，如果是None则停止，如果不是None，则继续遍历neighbors node"""
        if not node:
            return node

        if node in self.visited:        # 防止进入死循环，如果visited过则，直接return dictionary里面保存的node
            return self.visited[node]

        clone_node = Node(node.val, [])

        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node