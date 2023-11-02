# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node, visited):
        # 如果没有节点，返回 None
        if node is None:
            return None

        # 防止进入死循环，如果visited过则，直接return dictionary里面保存的node
        if node in visited:
            return visited[node]

        # 前序位置，做copy
        clone_node = Node(node.val, [])
        # 记录进visited字典
        visited[node] = clone_node

        if node.neighbors:
            for nei in node.neighbors:
                # 后序位置给当前节点赋值邻居节点
                clone_node.neighbors.append(self.dfs(nei, visited))

        # 返回节点，给上一层节点赋值
        return clone_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time O(n)
        Space O(n)
        DFS遍历图的写法，如果是None则停止，如果不是None，则继续遍历neighbors node，同时处理当前节点，
        在前序位置上clone，在后续位置上赋值邻居节点给当前节点。用visited字典，记录访问过的节点对应的clone节点。
        """
        visited = {}

        return self.dfs(node, visited)