# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> [TreeNode]:
        """类似后续遍历的操作，走到最下面的时候开始处理节点逻辑，在一次返回结果给上一层"""
        if not n:
            return []

        def generate_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)

                right_trees = generate_trees(i + 1, end)

                for l in left_trees:        # 走到这里说明当前节点对应的左右子树已经走完，开始构建连接
                    for r in right_trees:
                        current_node = TreeNode(i)
                        current_node.left = l
                        current_node.right = r
                        all_trees.append(current_node)     # 这里all_tree返回的是当前这一层节点对应的node，并已经构建左右树

            return all_trees
        # 最终返回的list里面是不同构造的树的root节点，ex: [node(1), node(2)], 节点里面已经构建完成左右子树
        return generate_trees(1, n)