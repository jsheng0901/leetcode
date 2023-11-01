from typing import List


class Solution:
    def __init__(self):
        self.validate_tree = True

    def dfs(self, node, left, right, visited):
        # 如果已经是不合理的，直接返回，不用继续递归
        if self.validate_tree is False:
            return

        # 如果走到树底，则直接返回
        if node == -1:
            return

        # 情况3：遇到走过的节点，说明有重复指向或者环，不合理的二叉树
        if visited[node]:
            self.validate_tree = False
            return

        # 标记当前节点访问过
        visited[node] = True

        # 递归左右子节点
        self.dfs(left[node], left, right, visited)
        self.dfs(right[node], left, right, visited)

        return

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """
        Time O(n)
        Space O(n)
        先找到整个二叉树的root，root是唯一的node不在child里面的节点。
        三种情况不符合标准二叉树的定义：
            1. 没有root
            2. 有的节点没有连接起来
            3. 有循环或者两个节点指向同一个子节点
        用DFS标记走过的节点，如果有重复的节点及走过的节点则不是合理二叉树，
        走完后check一遍是不是每个点都走到过，果然有遗漏的点也说明不是合理二叉树。
        """
        # 构建visited数组记录访问过
        visited = [False] * n
        # 查找root节点
        child_set = set(leftChild + rightChild)
        root = -1
        for i in range(n):
            if i not in child_set:
                root = i

        # 情况1：没有根节点，说明不是合理的二叉树
        if root == -1:
            return False

        # DFS loop 所有节点
        self.dfs(root, leftChild, rightChild, visited)

        # 情况2：检查是否有没有访问过的节点，及树断开
        res = False if not all(visited) else self.validate_tree

        return res


s = Solution()
print(s.validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
print(s.validateBinaryTreeNodes(n=4, leftChild=[3, -1, 1, -1], rightChild=[-1, -1, 0, -1]))
