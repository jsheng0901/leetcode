from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> Optional[ListNode]:
        """
        Time O(n)
        Space O(1)
        同234，一模一样，先找中间点，然后翻转后半部分，然后merge两个list
        find middle first then reversed second part then connect first and second part one by one
        """
        if not head:
            return None

        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            # 奇数指针指向偶数，并且奇数指针跳到下一个，用tmp指针记录原先list的下一个指针
            tmp = first.next
            first.next = second
            first = tmp
            # 偶数指针指向奇数，并且偶数指针跳到下一个
            tmp = second.next
            second.next = first
            second = tmp

        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
print(s.reorderList(node1).val)
