class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList_0(head: ListNode) -> ListNode:
    current = head
    previous = None
    while current:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp

    return previous


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
reverse_linked_list = reverseList_0(l1)
print(reverse_linked_list.val)
