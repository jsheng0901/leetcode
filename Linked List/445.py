# Definition for singly-linked list.
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
        O(n1+n2) time, O(1) space without output space
        reverse both list and add number forward
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
