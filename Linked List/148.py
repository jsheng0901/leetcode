# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, head1, head2):
        if head1 is None or head2 is None:
            return head2 or head1

        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head2 is None:
            cur.next = head1
        else:
            cur.next = head2

        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        """递归形式的拆分list，自底向上。每次拆分完就merge当前的左右部分list"""
        if head is None or head.next is None:
            return head

        pre = head
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

