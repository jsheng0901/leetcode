class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Time O(n)
        Space (1)
        pre作用是指针，永远在cur的后一个来改变next的指向，最后要判断一个哪一个先走完了，走完的还要用pre指针指向没走完的那一边
        """
        # 设计虚拟节点
        pre_node = ListNode(0)

        pre = pre_node
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            # 更新pre指针的位置，永远再cur的指针后面一个
            pre = pre.next

        if l1 is None:
            pre.next = l2
        else:
            pre.next = l1

        return pre_node.next
