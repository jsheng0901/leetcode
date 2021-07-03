class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head

        fast = dummy_node
        slow = dummy_node

        # 双指针写法，一定要让快指针先走到要删除的节点的前一个节点，然后快慢指针同时往前走，知道快指针走完所有node，此时慢指针刚好在要
        # 删除节点的前一个节点，之后就是改变连接节点，及删除

        while n + 1 > 0 and fast is not None:
            fast = fast.next
            n -= 1

        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy_node.next

