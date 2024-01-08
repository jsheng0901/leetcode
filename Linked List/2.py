from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time O(n)
        Space O(1)
        同时遍历两个linked list，用一个carry变量记录进位的数值是多少
        """
        dummy = ListNode(0)
        head = dummy

        carry = 0
        while l1 or l2 or carry != 0:
            curr_sum = carry
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next

            if curr_sum <= 9:
                dummy.val = curr_sum
                carry = 0
            else:
                dummy.val = curr_sum % 10
                carry = curr_sum // 10

            if l1 or l2 or carry != 0:
                dummy.next = ListNode(0)
                dummy = dummy.next

        return head


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(1)
        思路同上，只是不一样的写法
        """
        p1 = l1
        p2 = l2
        dummy_head = ListNode(-1)
        p = dummy_head
        carry = 0

        while p1 or p2 or carry != 0:
            cur_val = carry
            if p1:
                cur_val += p1.val
                p1 = p1.next
            if p2:
                cur_val += p2.val
                p2 = p2.next

            if cur_val > 9:
                node = ListNode(cur_val % 10)
                carry = cur_val // 10
            else:
                node = ListNode(cur_val)
                carry = 0

            # 这里也可以直接这样写，不需要判断
            # node = ListNode(cur_val % 10)
            # carry = cur_val // 10

            p.next = node
            p = p.next

        return dummy_head.next


l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(7)
l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6
s = Solution()
print(s.addTwoNumbers(l1, l3))
