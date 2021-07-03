class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy_head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.size - 1 or index < 0:
            return -1

        current = self.dummy_head.next     # star from node which after dummy head
        while index > 0:                   # loop over index
            current = current.next
            index -= 1

        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)                # create a new node
        new_node.next = self.dummy_head.next    # change new node next to dummy head next which mean skip dummy head
        self.dummy_head.next = new_node         # change dummy head back to new node as head, always make a dummy head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val)
        current = self.dummy_head   # start from dummy head always
        while current.next:         # find right now last node
            current = current.next
        current.next = new_node     # give last node new tail linked together
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        new_node = ListNode(val)     # create a new node
        current = self.dummy_head    # start from dummy head because index maybe will be 0 which means add new head
        while index > 0:
            current = current.next
            index -= 1
        new_node.next = current.next  # linked new node and current next node
        current.next = new_node       # linked current node to new node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.size - 1 or index < 0:
            return

        current = self.dummy_head      # start from dummy head since we want current node one ahead of delete node
        while index > 0:
            current = current.next
            index -= 1

        current.next = current.next.next    # right now current node is one ahead of index node which should be deleted
        self.size -= 1


obj = MyLinkedList()
param_1 = obj.get(0)
obj.addAtHead(2)
obj.addAtTail(4)
obj.addAtIndex(1, 5)
obj.deleteAtIndex(1)