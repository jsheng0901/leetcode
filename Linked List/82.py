class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        two pointers
        构建虚拟头结点，链接虚拟头节点和head，这样如果head也被删除的话，可以准确的找到下一个新的head node
        当找到下一个数和当前的数相同的时候，慢指针停止，快指针走到下一个不同的数，链接慢指针和快指针
        当下一个数不同的时候，快慢指针一起向前走
        """
        # 构建虚拟头结点
        dummy_head = ListNode(0)
        dummy_head.next = head
        # 快慢指针
        fast = head
        low = dummy_head

        while fast and fast.next:
            # 如果快指针下一个和当前相等，则loop循环走到下一个不相等的当前快指针
            if fast.next.val == fast.val:
                while fast.next and fast and fast.next.val == fast.val:
                    fast = fast.next
                # 这里要往前再跳一个，才能走到不是重复的快指针
                fast = fast.next
                # 慢指针在不重复的节点位置前一个，直接赋值
                low.next = fast
            else:
                # 快慢一起跳一步
                fast = fast.next
                low = low.next

        return dummy_head.next
