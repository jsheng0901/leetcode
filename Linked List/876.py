from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def get_length(self, node):

        length = 0
        while node:
            length += 1
            node = node.next

        return length

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(n + n/2)  -> O(n)
        Space O(1)
        先得到长度，然后计算出中间点的index，再走到这个index就是中点。但是需要遍历一次链表先。
        """
        # 得到长度
        length = self.get_length(head)

        # 计算中间点index
        middle = length // 2

        i = 0
        p = head
        # 走到中间点
        while i < middle:
            i += 1
            p = p.next

        return p


class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(1)
        双指针技巧，其实我们可以只遍历一次链表，只需要通过快慢指针，每当慢指针 slow 前进一步，快指针 fast 就前进两步，
        这样，当 fast 走到链表末尾时，slow 就指向了链表中点。
        """
        # 快慢指针初始化指向 head
        slow = fast = head
        # 快指针走到末尾时停止
        while fast and fast.next:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next

        # 慢指针指向中点
        return slow


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
s = Solution1()
print(s.middleNode(head=node1))
