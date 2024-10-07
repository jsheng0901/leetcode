class Bucket:
    def __init__(self):
        # 用数组来存储每一对key value，之后的增，删，查都可以达到O(1)的时间
        self.bucket = []

    def get(self, key):
        """
        Time O(bucket length)
        遍历bucket里面所有对，如果找到了就直接返回
        """
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        """
        Time O(bucket length)
        遍历bucket里面所有对，如果找到了就直接更新，没找到就append到最后
        """
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        """
        Time O(bucket length)
        遍历bucket里面所有对，如果找到了就直接删除
        """
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap1:

    def __init__(self):
        """
        Time O(n / k)   k is the number of predefined buckets, ex: 2069     n is the number of all possible keys
        Space O(m + k)  m is the number of unique keys
        利用数组来存储所有key value，先进行hash function映射，把key转化到到相对应的bucket里面。
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        # 初始化所有bucket
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        # 得到转化后的bucket index
        hash_key = key % self.key_space
        # 更新
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        # 同上
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        # 同上
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


class MyHashMap2:

    def __init__(self):
        """
        Time O(1)
        Space O(k)
        直接利用Python的自带的字典来implement
        """
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        """
        Time O(1)
        """
        self.hash_map[key] = value
        return

    def get(self, key: int) -> int:
        """
        Time O(1)
        """
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Time O(1)
        """
        if key in self.hash_map:
            del self.hash_map[key]


obj = MyHashMap1()
obj.put(key=1, value=1)
obj.put(key=2, value=2)
print(obj.get(key=1))
print(obj.get(key=3))
obj.put(key=2, value=1)
print(obj.get(key=2))
obj.remove(key=2)
print(obj.get(key=2))
