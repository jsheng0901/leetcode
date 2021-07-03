# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        O(n) time
        0(1) space
        """
        current = head  # start from firs head
        previous = None  # previous head node which is None at first
        while current:  # loop over linked node, when next is None then out
            tmp = current.next  # save current next node as temp node because this will be next current node
            current.next = previous  # point link back to previous node
            previous = current  # move previous to current node, this must move firs then current pointer
            current = tmp  # move current to temp node

        return previous

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
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
