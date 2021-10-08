# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """此题一定要记得顺序，逐个凉凉交换，dummy head尤其重要，当两个node跑完时，dummy head相当于前一个pair的尾"""
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur and cur.next and cur.next.next:
            first = cur.next        # 更新第一个
            second = first.next     # 更新第二个
            first.next = second.next    # 第一个指向下一个pair的第一个，此时原来的第一个节点变成下一个pair的dummy head
            second.next = first         # 翻转指向
            cur.next = second           # dummy head指向新的头结点
            cur = cur.next.next         # 更新current指针

        return dummy.next
