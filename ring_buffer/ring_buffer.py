class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.counter = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
           self.storage[self.counter] = item
           if self.counter + 1 == self.capacity:
               print('im here')
               self.counter = 0
           else:
               self.counter += 1
        else:
            self.storage.append(item)


    def get(self):
        return self.storage

buffer = RingBuffer(3)
buffer.append('d')
buffer.append('e')
buffer.append('f')
buffer.append('a')
buffer.append('v')
buffer.append('x')

print(buffer.storage)


