# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """同时遍历两个linked list，用一个carry变量记录进位的数值是多少"""
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



