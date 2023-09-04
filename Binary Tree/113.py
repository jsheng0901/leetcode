class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.result = []
        self.path = []

    def traversal(self, node, count):
        """
        Time O(n)
        Space O(n)
        后序遍历，count是用来判断当前node是否满足总和，用减法来判断，记录所有路径，则不需要返回数值在递归过程中
        每层处理当前node的子节点的value和path
        """
        if node.left is None and node.right is None and count == 0:
            self.result.append(self.path[:])    # deep copy path
            return
        if node.left is None and node.right is None:
            return

        if node.left:  # 每层处理当前node的子节点的value和path
            self.path.append(node.left.val)  # 递归
            count -= node.left.val  # 此处体现回溯的逻辑，减去后不满足这要加回来，等于回到上一个node
            self.traversal(node.left, count)
            count += node.left.val
            self.path.pop()

        if node.right:  # 每层处理当前node的子节点的value和path
            self.path.append(node.right.val)
            count -= node.right.val  # 此处体现回溯的逻辑，减去后不满足这要加回来，等于回到上一个node
            self.traversal(node.right, count)
            count += node.right.val
            self.path.pop()

        return

    def pathSum(self, root: TreeNode, targetSum: int) -> [[int]]:

        if root is None:
            return self.result

        self.path.append(root.val)
        self.traversal(root, targetSum - root.val)

        return self.result


class Solution2:
    def __init__(self):
        self.result = []
        self.path = []

    def traversal(self, node, value, target):
        """
        Time O(n)
        Space O(n)
        前序遍历的写法，value处理当前节点value，path处理当前下一个子节点value
        path list 无法像value一样，只处理当前层的节点，path list会随着传入下一层而改变之前层path list的value
        """
        if node.left is None and node.right is None:
            if target - value == node.val:
                path_copy = self.path.copy()
                self.result.append(path_copy)
                return
            else:
                return

        value += node.val  # 每层处理当前node的value和node的子节点path

        if node.left:
            self.path.append(node.left.val)
            self.traversal(node.left, value, target)
            self.path.pop()

        if node.right:
            self.path.append(node.right.val)
            self.traversal(node.right, value, target)
            self.path.pop()

        return

    def pathSum(self, root: TreeNode, targetSum: int) -> [[int]]:

        if root is not None:
            self.path.append(root.val)
            self.traversal(root, 0, targetSum)
            return self.result
        else:
            return self.result


class Solution3:
    def __init__(self):
        self.result = []

    def traversal(self, node, value, path, target):
        """
        Time O(n)
        Space O(n)
        前序遍历的写法，value处理当前节点value，path同时也处理当前节点value
        但path list会随着传入下一层而改变之前层path list的value，所以处理递归后要回溯pop out
        """
        value += node.val
        path.append(node.val)

        if node.left is None and node.right is None:
            if target == value:
                path_copy = path.copy()
                self.result.append(path_copy)
                return
            else:
                return

        if node.left:  # 每层处理当前node的value和当前node的path
            self.traversal(node.left, value, path, target)
            path.pop()  # 前序遍历在一开始就处理了添加，所以之后要回溯，回到前一个node节点

        if node.right:
            self.traversal(node.right, value, path, target)
            path.pop()

        return

    def pathSum(self, root: [TreeNode], targetSum: int) -> [[int]]:
        if root:
            self.traversal(root, 0, [], targetSum)

        return self.result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
solution = Solution3()
print(solution.pathSum(t1, 5))
