class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition1(self, head: ListNode, x: int) -> ListNode:
        print('this is method 1')
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        p1 = dummy1
        p2 = dummy2
        cur = head

        while cur:
            if cur.val < x:
                p1.next = cur
                p1 = cur
            else:
                p2.next = cur
                p2 = cur

            cur = cur.next
        # 一定要check最后哪一个是尾巴，并且指向None不然会return出死循环
        if p1.next is not None:
            p1.next = None
        if p2.next is not None:
            p2.next = None

        p1.next = dummy2.next

        return dummy1.next

    def partition2(self, head: ListNode, x: int) -> ListNode:
        """
        three pointers, first record position of smaller than x, second record position of bigger or equal than x,
        third is loop whole linked node
        当找到小与x的node时候就记录一下position，并更新链接，同理对于大于x的node
        :param head:
        :param x:
        :return:
        """
        p1, p2 = None, None
        cur = head

        while cur:
            if cur.val < x:
                if p1 is None:
                    p1_head = cur
                    p1 = cur
                else:
                    p1.next = cur
                    p1 = cur
            else:
                if p2 is None:
                    p2_head = cur
                    p2 = cur
                else:
                    p2.next = cur
                    p2 = cur

            cur = cur.next

        if p1 is None or p2 is None:    # which mean no manipulate or change with original linked node
            return head
        else:
            p1.next = p2_head           # connect last small part node to first bigger part node
            p2.next = None              # cut bigger part last node link

            return p1_head


node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
s = Solution()
print(s.partition1(node1, 3))