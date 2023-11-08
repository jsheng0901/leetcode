from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.height = None

    def traversal(self, node, query, cur_height):
        """
        前序遍历查找最深深度，开全局变量记录深度，一直走到底，一直更新深度，如果遇到空节点就停止。
        遇到query节点也停止，意味着不能向下走path。
        """
        if node is None:
            return

        if node.val == query:
            return
        # 当前节点深度，对应的最深深度
        self.height = max(self.height, cur_height)
        self.traversal(node.left, query, cur_height + 1)
        self.traversal(node.right, query, cur_height + 1)

        return

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """
        Time O(n * q)
        Space O(n)
        每一个query去前序遍历一遍树，每次遍历找到最深深度即可。超时对于节点多并且query多查询。近似 -> O(n^2)。
        """
        ans = []
        for query in queries:
            self.height = 0
            self.traversal(root, query, 0)
            ans.append(self.height)

        return ans


class Solution2:
    def __init__(self):
        self.ans = None

    def traversal(self, node, query_to_index, cur_height, query_status):
        if node is None:
            for i in range(len(self.ans)):
                if query_status[i]:
                    continue
                else:
                    self.ans[i] = max(self.ans[i], cur_height - 1)
            return

        node_in_query = True if node.val in query_to_index else False
        if node_in_query:
            index_list = query_to_index[node.val]
            for i in index_list:
                query_status[i] = True
                self.ans[i] = max(self.ans[i], cur_height - 1)

        self.traversal(node.left, query_to_index, cur_height + 1, query_status)
        self.traversal(node.right, query_to_index, cur_height + 1, query_status)

        if node_in_query:
            for i in index_list:
                query_status[i] = False

        return

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """
        Time O(n * number leaf)
        Space O(n)
        同样的思路，但是我们只遍历一次树，用一个等长度query的数组记录在每个path时候是否遇到了query节点，
        每次遍历的时候经过的当前节点，判断是否是query节点，如果是
        说明此path对应的此query不能向下走了，记录状态的数组标记为找此query节点，之后则不再更新此query节点的深度，同时记录到当前最深深度，
        继续遍历到底，在更新整个result数组记录全局最深深度对应每个query节点。详细思路见注释，此方法依旧超时，因为当query很大的时候，
        leaf很多的时候每个leaf都需要一个O(query)，则很容易超时。
        """
        query_to_index = defaultdict(list)
        for i in range(len(queries)):
            query_to_index[queries[i]].append(i)

        self.ans = [0] * len(queries)
        query_status = [False] * len(queries)
        self.traversal(root, query_to_index, 0, query_status)

        return self.ans


class Solution3:
    def postorder(self, node):
        """
        后续遍历记录每个节点深度，用返回值的方式更新节点深度，此处叶子节点深度为0。
        """
        # 空节点，返回 -1，因为叶子节点深度为 0
        if node is None:
            return -1

        # 左子树结果
        left = self.postorder(node.left)
        # 右子树结果
        right = self.postorder(node.right)
        # 最大深度加上当前节点深度 +1
        max_height = max(left, right) + 1
        # 更新进当前节点记录下来
        node.val = [node.val, max_height]
        # 返回当前节点最大深度
        return max_height

    def preorder(self, node, depth, max_height, node_to_height):
        # 遇到空节点结束递归
        if node is None:
            return
        # 当前节点的全局最大深度
        node_to_height[node.val[0]] = max_height
        # 右子树的最大深度为，此时的深度或者父节点传入过来左子树的最大深度，为全局最大深度，
        # 此情况是当右子树不存的时候，我们需要对比父节点传过来的最大深度和当前深度
        right_max_height = max(max_height, depth)
        # 同理右子树
        left_max_height = max(max_height, depth)
        # 如果右子树存在
        if node.right:
            # 那么右子树最大深度为，父节点传过来的最大深度，或者当前节点的右子树节点对应的之前后续遍历找到的深度 + 当前深度 + 1
            right_max_height = max(max_height, depth + 1 + node.right.val[1])
        # 同上
        if node.left:
            left_max_height = max(max_height, depth + 1 + node.left.val[1])
        # 递归左右子树，这里左子树，传输过去的应该是右子树的最大全局深度，同理右子树的传输
        self.preorder(node.left, depth + 1, right_max_height, node_to_height)
        self.preorder(node.right, depth + 1, left_max_height, node_to_height)

        return

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        此方法很巧妙的地方在于，对于每个节点，能在全局达到的最深深度，为当前节点走到底的深度，或者兄弟节点分支的父节点的最深深度。
        此时我们需要的只是把每个节点到树底的深度先算出来并记录下来。在前序遍历的时候记录当前节点在全局的最深深度，用字典记录起来，
        query需要查找的即为query节点在全局的最深深度。
        """
        # 后续遍历记录深度进每个节点
        self.postorder(root)
        # 构建节点到高度的字典
        node_to_height = {}
        # 前序遍历记录节点全局高度
        self.preorder(root, 0, 0, node_to_height)
        # 直接提取我们需要遍历的query
        ans = [node_to_height[i] for i in queries]

        return ans


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node5.left = node4
node5.right = node6
node4.left = node2
node2.left = node1
node2.right = node3
node6.right = node8
node8.left = node7
s = Solution3()
print(s.treeQueries(node5, queries=[8]))
