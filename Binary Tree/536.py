# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_number(self, s, index):
        is_negative = False

        if s[index] == '-':
            is_negative = True
            index += 1

        number = 0
        while index < len(s) and s[index].isdigit():
            number = 10 * number + int(s[index])
            index += 1

        return number if not is_negative else -number, index

    def traversal(self, s, index):
        if index == len(s):
            return None, index

        value, index = self.get_number(s, index)
        node = TreeNode(value)

        if index < len(s) and s[index] == '(':
            node.left, index = self.traversal(s, index + 1)

        if node.left and index < len(s) and s[index] == '(':
            node.right, index = self.traversal(s, index + 1)

        if index < len(s) and s[index] == ')':
            return node, index + 1
        else:
            return node, index
        # return node, index + 1 if index < len(s) and s[index] == ')' else index

    def str2tree(self, s: str) -> [TreeNode]:
        """
        像前序遍历，每次先往左边走，每一个做到下一个的时候index+1， 每一次拿完一个数字的时候，
        return回来的index是进去index+1的结果
        """
        return self.traversal(s, 0)[0]



