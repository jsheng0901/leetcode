# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head  # start from firs head
        previous = None  # previous head node which is None at first
        while current:  # loop over linked node, when next is None then out
            tmp = current.next  # save current next node as temp node because this will be next current node
            current.next = previous  # point link back to previous node
            previous = current  # move previous to current node, this must move firs then current pointer
            current = tmp  # move current to temp node

        return previous

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        Time O(n)
        Space 0(1)
        找到区间的起点和终点，切断起点前一个节点和起点的关系，反正新的起点节点，并后续连接起来。详细见注释。
        """
        tmp = ListNode()    # 构建dummy header
        tmp.next = head     # dummy header指向原始header
        cur = tmp           # 找到当前current header

        for i in range(right):
            if i == left - 1:   # 找到left node前一个node并且记录
                left_node = cur
            cur = cur.next

        right_node = cur.next   # 循环结束时候下一个node就是right后面一个node，并记录

        cur.next = None         # 切断当前是right node的后序连接
        new_head = left_node.next   # 新的需要reverse的部分的header
        left_node.next = None       # 切断原来left node前一个node的连接
        left_node.next = self.reverseList(new_head)   # reverse需要的部分并且return reverse之后的header，并连接left前一个node
        new_head.next = right_node                    # 原来的new header就是现在reverse之后的last node，连接原先的right后面一个

        return tmp.next     # return 原来的header


class Solution2:
    def __init__(self):
        self.successor = None  # 后驱节点

    def reverse_n(self, head: ListNode, n: int) -> ListNode:
        # 同206题写法，只是这里是前n个节点而不是所有节点
        # 反转以 head 为起点的 n 个节点，返回新的头结点
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head

        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverse_n(head.next, n - 1)

        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor

        return last

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(n)
        递归的思路写，本质上是把反转前n个链表和反转一个区间内的链表组合起来一起写。详细见注释
        """
        # base case
        if left == 1:
            return self.reverse_n(head, right)

        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left - 1, right - 1)

        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
print(s.reverseBetween(node1, 2, 4))
