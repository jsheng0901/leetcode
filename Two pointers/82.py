# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """快慢指针同时异动如果快指针下一个和现在value不同的时候，如果相同，快指针直到走到下一个不同的时候，慢指针连接快指针"""
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head

        while fast and fast.next:
            if fast.next.val == fast.val:
                while fast and fast.next and fast.next.val == fast.val:
                    fast = fast.next
                fast = fast.next
                slow.next = fast
            else:
                fast = fast.next
                slow = slow.next

        return dummy.next
