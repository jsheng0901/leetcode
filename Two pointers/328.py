class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        此题必须两个pointer同时遍历，不可一个遍历完在遍历另一个，因为一个遍历完之后p.next.next的值就变了，不再是之前的偶数index对应点了
        会进入死循环，所以一起交替遍历
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head

        p1 = head
        p2 = head.next
        even_head = head.next

        while p1.next and p2.next:
            p1.next = p2.next
            p1 = p2.next
            p2.next = p1.next
            p2 = p1.next

        p1.next = even_head

        return head