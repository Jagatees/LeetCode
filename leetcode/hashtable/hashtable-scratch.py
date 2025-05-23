class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        total = 0
        prime = 31
        for i in range(min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96  # assuming key is lowercase alphabetic
            total = (total * prime + value) % self.size
        return total
    

    def set(self, key, value):
        index = self._hash(key)
        self.table[index].append((key,value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        if bucket:
            for k, v in bucket:
                if k == key:
                    return v
        
        return self.table[index]
    

    def keys(self):
        keysArray = []
        for bucket in self.table:
            for k, v in bucket:
                keysArray.append(k)
        return keysArray


ht = HashTable()
ht.set("apple", 10)
ht.set("grape", 20)
ht.set("banana", 30)
# print(ht.get("grape"))
# print(ht.table)
print(ht.keys())
        
# if no collesion then 0(1)