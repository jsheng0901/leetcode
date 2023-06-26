class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        time: O(n)
        space: O(1)
        """
        p1 = headA
        p2 = headB

        while p1 != p2:
            if p1 is not None:
                p1 = p1.next
            else:
                p1 = headB

            if p2 is not None:
                p2 = p2.next
            else:
                p2 = headA

        return p1

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        time: O(n)
        space: O(1)
        先找到两个链表的长度，然后让长的链表走到和短链表的相同位置，
        然后同时两个链表一起走check是否有相同node，没有则返回None，有则返回node
        """
        p1 = headA
        p2 = headB
        l_a = 0
        l_b = 0

        while p1:
            p1 = p1.next
            l_a += 1

        while p2:
            p2 = p2.next
            l_b += 1

        new_p1 = headA
        new_p2 = headB
        if l_a >= l_b:
            diff = l_a - l_b
            while diff > 0:
                new_p1 = new_p1.next
                diff -= 1

            while new_p1 != new_p2 and new_p1 is not None and new_p2 is not None:
                new_p1 = new_p1.next
                new_p2 = new_p2.next

            return new_p1 if new_p1 is not None else None
        else:
            diff = l_b - l_a
            while diff > 0:
                new_p2 = new_p2.next
                diff -= 1

            while new_p1 != new_p2 and new_p1 is not None and new_p2 is not None:
                new_p1 = new_p1.next
                new_p2 = new_p2.next

            return new_p2 if new_p2 is not None else None
