from collections import OrderedDict
from typing import Union


class LRUCache1:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache[key]
        self.cache.pop(key)  # remove the key first
        self.cache[key] = value  # add this key to end of orderedDict
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache.keys()) == self.capacity:
                self.cache.popitem(last=False)  # always pop first item in orderedDict

            self.cache[key] = value


class LRUCache2:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Time O(1)
        同上只是调用了ordereddict里面内置的 move to end function
        """
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        if len(self.cache) >= self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value


# use double link list and dict to implement orderedDict
class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # 在链表尾部添加节点 x，时间 O(1)
    def add_last(self, x: Node):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    # 删除链表中的 x 节点（x 一定存在）
    # 由于是双链表且给的是目标 Node 节点，时间 O(1)
    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    # 删除链表中第一个节点，并返回该节点，时间 O(1)
    def remove_first(self) -> Union[None, Node]:
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first


class LRUCache:
    def __init__(self, capacity: int):
        """
        key -> Node(key, val)
        创建一个哈希表将 Node 节点的 key 映射至其本身
        map: dict[int, Node]

        Node(k1, v1) <-> Node(k2, v2)...
        双向链表用来实现 LRU 缓存淘汰机制
        cache: DoubleList

        最大容量
        缓存最大容量，超过此容量则淘汰
        cap: int
        """
        self.cap = capacity
        self.map = {}
        self.cache = DoubleList()

    def make_recently(self, key: int):
        # 将某个 key 提升为最近使用的
        x = self.map.get(key)
        # 先从链表中删除这个节点
        self.cache.remove(x)
        # 重新插到队尾
        self.cache.add_last(x)

    def add_recently(self, key: int, val: int):
        # 添加最近使用的元素
        x = Node(key, val)
        # 链表尾部就是最近使用的元素
        self.cache.add_last(x)
        # 别忘了在 map 中添加 key 的映射
        self.map[key] = x

    def delete_key(self, key: int):
        # 删除某一个 key
        x = self.map.get(key)
        # 从链表中删除
        self.cache.remove(x)
        # 从 map 中删除
        self.map.pop(key)

    def remove_least_recently(self):
        # 删除最久未使用的元素
        # 链表头部的第一个元素就是最久未使用的
        deleted_node = self.cache.remove_first()
        # 同时别忘了从 map 中删除它的 key
        deleted_key = deleted_node.key
        self.map.pop(deleted_key)

    def get(self, key: int) -> int:
        # 读操作
        if key not in self.map:
            return -1
        self.make_recently(key)
        return self.map.get(key).val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.get(key).val = value
            self.make_recently(key)
            return
        if self.cache.size == self.cap:
            self.remove_least_recently()
        self.add_recently(key, value)


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
