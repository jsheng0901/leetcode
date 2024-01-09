# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def inverse(self, head):
        pre = None
        p1 = head
        while p1:
            tmp = p1.next
            p1.next = pre
            pre = p1
            p1 = tmp

        return pre

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        """
        Time O(n1 + n2),
        Space O(1)
        先翻转，然后再叠加，和题目2一样。
        """
        l1_new_head = self.inverse(l1)
        l2_new_head = self.inverse(l2)

        p1 = l1_new_head
        p2 = l2_new_head
        head = None
        carry = 0
        while p1 or p2:
            x1 = p1.val if p1 else 0
            x2 = p2.val if p2 else 0
            val = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10

            curr = ListNode(val)
            curr.next = head
            head = curr

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if carry > 0:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(n1 + n2)
        Space O(n1 + n2)
        用栈来存储数据，因为先进后出，所以自动进行从后向前的叠加，叠加部分和题目2一样。
        """
        # 把链表元素转入栈中
        stack1 = []
        stack2 = []
        p1 = l1
        p2 = l2

        while p1:
            stack1.append(p1.val)
            p1 = p1.next
        while p2:
            stack2.append(p2.val)
            p2 = p2.next

        # 接下来基本上是复用第 2 题的代码逻辑
        # 注意新节点要直接插入到 dummy 后面
        # 虚拟头结点（构建新链表时的常用技巧）
        # 记录进位
        carry = 0
        dummy_head = ListNode(-1)

        # 开始执行加法，两条链表走完且没有进位时才能结束循环
        while stack1 or stack2 or carry:
            # 先加上上次的进位
            cur_value = carry
            if stack1:
                cur_value += stack1.pop()
            if stack2:
                cur_value += stack2.pop()
            # 处理进位情况
            value = cur_value % 10
            carry = cur_value // 10

            # 构建新节点，直接接在 dummy 后面
            node = ListNode(value)
            node.next = dummy_head.next
            dummy_head.next = node

        # 返回结果链表的头结点（去除虚拟头结点）
        return dummy_head.next


l1 = ListNode(7)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(3)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l5.next = l6
l6.next = l7
s = Solution()
print(s.addTwoNumbers(l1, l5))
