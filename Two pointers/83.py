# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """双指针，不相等同时跳，相等则fast一直走到不相等，连接slow 和 fast，继续同时向前跳"""
        if head is None:
            return head

        current = head.next
        prev = head

        while current:
            if current.val == prev.val:
                if current.next is None:
                    prev.next = None
                current = current.next
            else:
                prev.next = current
                prev = prev.next
                current = current.next

        return head