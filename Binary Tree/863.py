# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node, par=None):
        if node:
            node.par = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)
        return

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> [int]:
        """先做dfs转化成graph，然后bsf查找距离"""
        self.dfs(root)

        queue = [(target, 0)]
        seen = {target}

        while len(queue) > 0:
            if queue[0][1] == k:
                return [node.val for node, d in queue]

            node, d = queue.pop(0)
            for neig in (node.left, node.right, node.par):
                if neig and neig not in seen:
                    seen.add(neig)
                    queue.append((neig, d + 1))

        return []


