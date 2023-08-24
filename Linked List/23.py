from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1, l2):
        prev_node = ListNode(0)
        prev = prev_node

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next = l1

        return prev_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        if len(lists) == 1 and lists[0] is None:
            return None

        if len(lists) == 1:
            return lists[0]

        new_head = self.merge_two_lists(lists[0], lists[1])

        for i in range(2, len(lists)):
            new_head = self.merge_two_lists(new_head, lists[i])

        return new_head
