class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList_0(head: ListNode) -> ListNode:
    """
    O(n) time
    0(1) space
    """
    current = head      # start from firs head
    previous = None     # previous head node which is None at first
    while current:      # loop over linked node, when next is None then out
        tmp = current.next       # save current next node as temp node because this will be next current node
        current.next = previous  # point link back to previous node
        previous = current       # move previous to current node, this must move firs then current pointer
        current = tmp            # move current to temp node

    return previous              # return new head


def reverse(pre, cur):
    if cur is None:
        return pre
    temp = cur.next
    cur.next = pre
    # 可以和双指针法的代码进行对比，如下递归的写法，其实就是做了这两步
    # pre = cur;
    # cur = temp;

    return reverse(cur, temp)


def reverseList_1(head: ListNode) -> ListNode:
    pre = None   # 初始化过程和two pointer 一样
    cur = head

    return reverse(pre, cur)


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
reverse_linked_list = reverseList_1(l1)
print(reverse_linked_list.val)