class array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    
    def delete(self, index):
        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return item



arr = array()
print(arr.push("1"))
print(arr.get(0))
print(arr.pop())


# Fast Lookups
# Fast push/pop
# Ordered

# Slow inserts
# Slow deletes
# Fixed size 
# *if using static array
