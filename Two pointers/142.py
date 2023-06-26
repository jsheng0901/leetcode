class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle1(head: ListNode) -> ListNode:
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            index1 = head
            index2 = fast
            while index1 != index2:
                index1 = index1.next
                index2 = index2.next

            return index1

    return -1


def detectCycle2(head: ListNode) -> ListNode:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast is None or fast.next is None:
        return None

    index1 = head
    index2 = fast

    while index1 != index2:
        index1 = index1.next
        index2 = index2.next

    return index1


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2
print(detectCycle1(l1).val)
