# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        只需要把给定要删除的node的下一个node的value替换过来，同时替换此时node的next到下一个node的next next
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is not None:
            node.val, node.next = node.next.val, node.next.next
