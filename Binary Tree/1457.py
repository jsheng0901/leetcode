from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def is_pseudo_palindromic(self, path):
        odd_number = 0

        for i in range(1, len(path)):
            if path[i] % 2 != 0:
                odd_number += 1

                if odd_number > 1:
                    return False

        return odd_number == 1 or odd_number == 0

    def traversal(self, node, path):
        # 遇到空节点
        if node is None:
            return

        # 遇到叶子结点
        if node.left is None and node.right is None:
            # 记录叶子结点频率
            path[node.val] += 1
            # 检查是否是回文
            if self.is_pseudo_palindromic(path):
                # 计数器 +1
                self.res += 1
            # 离开当前叶子节点，回溯
            path[node.val] -= 1
            return

        # 记录当前节点频率
        path[node.val] += 1

        self.traversal(node.left, path)
        self.traversal(node.right, path)

        # 离开当前节点，回溯
        path[node.val] -= 1

        return

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)       since path is constant length no more than 10
        Space O(h)
        前序遍历存储所有节点的值出现的频率，走到叶子节点的时候check是否所有出现的频率只有一个奇数或者没有奇数，如果是则说明是
        pseudo palindromic。同时计数器 +1，如果不是结束此path的search。注意这里因为要一直记录出现的频率，离开此节点的时候要回溯一下，
        因为另一条path不可能包含此节点的值。
        """
        path = [0] * 10
        self.traversal(root, path)

        return self.res


node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(3)
node6 = TreeNode(2)
node6.left = node4
node6.right = node1
node4.left = node5
node4.right = node2
node1.right = node3
s = Solution()
print(s.pseudoPalindromicPaths(node6))
