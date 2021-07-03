# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int) -> ListNode:
    dummy_head = ListNode(0)    # 构建一个虚拟head，并赋值为0
    dummy_head.next = head      # 连接虚拟head和真正的head

    current = dummy_head        # 此时的linked list head是虚拟head

    while current and current.next:     # 循坏走遍linked list
        if current.next.val == val:     # 如果下一个node的值和给定的value一样，则连接此时的node和next到下下个node
            current.next = current.next.next
        else:
            current = current.next      # 否则此时的node等于下一个连接node，及跟随linked list往前跳一个node

    return dummy_head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
final_linked_list = removeElements(l1, 2)
print(final_linked_list.val)
print(final_linked_list.next.val)