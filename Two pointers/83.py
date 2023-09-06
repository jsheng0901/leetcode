from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def deleteDuplicates(self, head: ListNode) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(1)
        双指针，不相等同时跳，相等则fast一直走到不相等，连接slow 和 fast，继续同时向前跳
        """
        if head is None:
            return head

        current = head.next
        prev = head

        while current:
            if current.val == prev.val:
                if current.next is None:
                    # 断开与后面重复元素的连接
                    prev.next = None
                current = current.next
            else:
                prev.next = current
                prev = prev.next
                current = current.next

        return head


class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        同上写法，区别在于起始点这次两个指针一样。断开与后面节点的处理方式不一样。
        """
        if head is None:
            return head

        slow = head
        fast = head

        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next

        # 断开与后面重复元素的连接
        slow.next = None

        return head
