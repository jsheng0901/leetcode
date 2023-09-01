from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.result = []

    def traversal(self, node, to_delete):
        # 走到叶子节点，直接返回None
        if node is None:
            return node
        # 判断是否需要被删除。
        if node.val in to_delete:
            # 判断左右子树是否存在。
            if node.left:
                # 如果子树存在需要判断是否要被删除，否则会加入进最终结果。
                if node.left.val not in to_delete:
                    self.result.append(node.left)
                # 遍历子树
                self.traversal(node.left, to_delete)
            if node.right:
                if node.right.val not in to_delete:
                    self.result.append(node.right)
                self.traversal(node.right, to_delete)
            # 返回空节点，同时执行删除操作，赋值给父节点。
            return None
        else:
            # 不需要则递归左右子树，并赋值
            node.left = self.traversal(node.left, to_delete)
            node.right = self.traversal(node.right, to_delete)
            return node

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        Time O(n)
        Space O(n)
        前序遍历，每次判断当前节点是否需要被删除，如果需要就判断左右子树是否存在并且需要被删除，然后递归判断子树，
        如果不需要被删除则直接返回node本身，并通过递归函数返回值赋值给父节点。
        """
        # 判断一下根节点是否需要被删除，不需要则加入结果
        if root.val not in to_delete:
            self.result.append(root)

        self.traversal(root, to_delete)

        return self.result


class Solution2:
    def __init__(self):
        self.result = []

    def traversal(self, node, to_delete):
        if node is None:
            return node

        node.left = self.traversal(node.left, to_delete)
        node.right = self.traversal(node.right, to_delete)

        if node.val in to_delete:
            # 区别在此，不再需要判断左右子树在不在删除list里面，后续遍历先拿到左右子树的处理结果，已返回None如果需要被删除
            if node.left:
                self.result.append(node.left)

            if node.right:
                self.result.append(node.right)

            return None

        return node

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        Time O(n)
        Space O(n)
        后续遍历，每次判断当前节点是否需要被删除，
        1.  如果需要就判断左右子树是否存在，存在则直接接入结果，然后递归判断子树，区别与前序遍历在，
            不需要判断左右子树是否要被删除，因为左右子树的结果已经在后续遍历处理中间节点前结束了，如果需要被删除，左右子树返回值已经是None了，
            则判断是否存在就可以，不再需要check在不在删除的list里面。
        2.  如果不需要被删除则直接返回node本身，并通过递归函数返回值赋值给父节点。
        """
        if root.val not in to_delete:
            self.result.append(root)

        self.traversal(root, to_delete)

        return self.result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node4
node4.right = node3
s = Solution1()
print(s.delNodes(node1, to_delete=[3]))
