from collections import defaultdict, deque


class LFUCache:

    def __init__(self, capacity: int):
        # key 到 val 的映射
        self.key_2_val = defaultdict(int)
        # key 到 freq 的映射
        self.key_2_freq = defaultdict(int)
        # freq 到 key 列表的映射，这里使用双向列队，因为第一个元素是LRU元素，也就是我们需要弹出的元素当频率一样的时候
        self.freq_2_keys = defaultdict(deque)
        # 记录最小的频次
        self.min_freq = 0
        # 记录 LFU 缓存的最大容量
        self.cap = capacity

    def increase_freq(self, key):
        # 拿到之前的key的频率
        old_freq = self.key_2_freq[key]
        # 新的频率
        new_freq = old_freq + 1
        # 更新 key freq 字典
        self.key_2_freq[key] = new_freq

        # 将 key 从之前频率对应的列队中删除
        self.freq_2_keys[old_freq].remove(key)
        # 将 key 加入新频率对应的列表中
        self.freq_2_keys[new_freq].append(key)
        # 如果 freq 对应的列表空了，移除这个 freq
        if not self.freq_2_keys[old_freq]:
            del self.freq_2_keys[old_freq]
            # 如果这个 freq 恰好是 min_freq，更新 min_freq
            if old_freq == self.min_freq:
                self.min_freq += 1

    def remove_min_freq_key(self):
        # freq 最小的 key 列表
        key_list = self.freq_2_keys[self.min_freq]
        # 其中最先被插入的那个 key 就是该被淘汰的 key，也就是列队头
        delete_key = key_list.popleft()

        # 如果列队只有一个元素并弹出后，删除对应的key
        if not key_list:
            del self.freq_2_keys[self.min_freq]

        # 删除对应的 key value
        del self.key_2_val[delete_key]
        # 删除对应的 key freq
        del self.key_2_freq[delete_key]

    def get(self, key: int) -> int:
        """
        Time O(1)
        全都是字典或者双向列队添加的操作
        """
        # 如果不存在，直接返回 -1
        if key not in self.key_2_val:
            return -1

        # 增加 key 对应的 freq
        self.increase_freq(key)

        # 返回存在的key的频率
        return self.key_2_val[key]

    def put(self, key: int, value: int) -> None:
        """
        Time O(1)
        全都是字典或者双向列队添加和弹出的操作
        """
        if self.cap <= 0:
            return

        # 若 key 已存在，修改对应的 val 即可
        if key in self.key_2_val:
            # 更新 value
            self.key_2_val[key] = value
            # 增加 key 对应的 freq
            self.increase_freq(key)
            return

        # key 不存在，需要插入
        # 容量已满的话需要淘汰一个 freq 最小的 key
        if self.cap <= len(self.key_2_val):
            self.remove_min_freq_key()

        # 新的 key value
        # 插入 key 和 val 字典
        self.key_2_val[key] = value
        # 插入对应的 freq 为1的字典
        self.key_2_freq[key] = 1
        # 插入对应频率 key的字典，并加入到列队尾巴，表示最近使用的key
        self.freq_2_keys[1].append(key)
        # 插入新 key 后最小的 freq 肯定是 1
        self.min_freq = 1


obj = LFUCache(2)
obj.put(2, 1)
obj.put(3, 2)
print(obj.get(3))
print(obj.get(2))
obj.put(4, 3)
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
