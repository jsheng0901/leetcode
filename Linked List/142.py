class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycle(head: ListNode) -> ListNode:
    """
     O(n) time, loop cycle n times if has cycle, if not then n is length of linked list
     此题有一定数学知识，先找到是否有环，再找到环的入口，找是否有环靠快慢指针，快指针是慢指针两倍的频率，找入口靠相遇node和head node同一个频率
    """
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # 快慢指针相遇，此时从head和相遇点，同时查找直至相遇
        if fast == slow:    # 此时快慢指针在同一个node
            index1 = fast
            index2 = head
            while index1 != index2:    # 此时index1 index2指针往前走的步数一致
                index1 = index1.next
                index2 = index2.next

            return index1      # return cycle entrance

    return None


def detectCycle(head: ListNode) -> ListNode:
    """
     O(n) time, 额外 set空间
     此方法利用set不能重复的原理，如果有环的入口，那么set一定有重复，我们return重复的node就行
    """
    if head is None:
        return None

    hash_set = set()
    cur = head
    while cur:
        if cur in hash_set:
            return cur
        else:
            hash_set.add(cur)
            cur = cur.next

    return None


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l1
print(detectCycle(l1).val)