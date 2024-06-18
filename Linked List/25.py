from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 反转以 a 为头结点的链表模版写法
# def reverse(a: ListNode) -> ListNode:
#     pre, cur, nxt = None, a, a
#     while cur:
#         nxt = cur.next
#         # 逐个结点反转
#         cur.next = pre
#         # 更新指针位置
#         pre = cur
#         cur = nxt
#     # 返回反转后的头结点
#     return pre

class Solution:
    def reverse(self, a: ListNode, b: ListNode) -> ListNode:
        pre, cur, nxt = None, a, a
        # while 终止的条件改一下就行了对比模板
        while cur != b:
            # 先存一下原始链表中的的下一个节点，否则后续反转后会找不到原始的下一个节点
            nxt = cur.next
            # 逐个结点反转
            cur.next = pre
            # 更新指针位置
            pre = cur
            cur = nxt

        # 返回反转后的头结点
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(n/k)
        通过递归的写法，类似树的后续遍历，每次当前区间的头结点赋值给递归函数返回值为当前区间反转后新的头结点。详细见注释
        """
        # 如果没有头节点，返回空节点，对于最后一个区间的旧的头结点赋值空节点
        if not head:
            return None

        # 双指针区间 [a, b) 包含 k 个待反转元素
        a = head
        b = head
        for i in range(k):
            # 不足 k 个，不需要反转，直接返回当前区间的原始头结点，base case
            if not b:
                return head
            # 找到区间 [a, b) 中的b
            b = b.next

        # 反转前 k 个元素，并返回新的头节点
        new_head = self.reverse(a, b)
        # 递归反转后续链表并连接起来，原始头节点链接下一个区间的新头结点，类似后续遍历赋值的地方
        a.next = self.reverseKGroup(b, k)
        # 返回新节点
        return new_head


head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(5)
head1.next = head2
head2.next = head3
head3.next = head4
head4.next = head5
s = Solution()
print(s.reverseKGroup(head=head1, k=2))
