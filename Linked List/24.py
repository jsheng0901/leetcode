# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Time O(n)
        Space O(1)
        此题一定要记得顺序，逐个两两交换，dummy head尤其重要，当两个node跑完时，dummy head相当于前一个pair的尾
        第一步：翻转第一个节点指向第三节点
        第二步：翻转第二节点指向第一节点
        第三步：dummy指针指向第二节点
        第四步：更新dummy指针为原来的第一节点
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur and cur.next and cur.next.next:
            first = cur.next            # 记录没有转换前第一个
            second = first.next         # 记录没有转换前第二个
            first.next = second.next    # 第一个指向下一个pair的第一个，此时原来的第一个节点变成下一个pair的dummy head
            second.next = first         # 翻转指向
            cur.next = second           # dummy head指向新的头结点
            cur = cur.next.next         # 更新current指针

        return dummy.next


class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        另一种交换顺序
        第一步：dummy指针指向第二节点
        第二步：翻转第二节点指向第一节点
        第三步：翻转第一个节点指向第三节点
        第四步：更新dummy指针为原来的第一节点
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            tmp1 = cur.next             # 记录没有转换前第一个
            tmp2 = cur.next.next.next   # 记录没有转换前第三个

            cur.next = cur.next.next    # 第一步
            cur.next.next = tmp1        # 第二步
            tmp1.next = tmp2            # 第三步
            cur = tmp1                  # 第四步

        return dummy.next
