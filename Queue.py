# FIFO

class Queue:
    # Circular Queue
    def __init__(self, size=100):
        if size < 1: size = 1
        self._queue = [None] * size
        self.rear = -1
        self.front = -1
        self.length = 0 # current length of queue

    def is_full(self):
        return self.length >= len(self._queue)
    
    def enqueue(self, data):
        if self.is_full(): 
            print('Queue is Full!')
            return None
        if self.is_empty():
            self.front = self.rear = 0
        else: self.rear = (self.rear + 1) % len(self._queue)
        self._queue[self.rear] = data
        self.length += 1
        return self._queue[self.rear]

    def dequeue(self):
        if self.is_empty(): return None
        el = self._queue[self.front]
        self.front = (self.front + 1) % len(self._queue)
        self.length -= 1
        return el

    def is_empty(self):
        return self.length < 1

    def peek(self):
        if self.is_empty(): return None
        return self._queue[self.front]

    def __repr__(self) -> str:
        if self.is_empty(): return 'EMPTY QUEUE!'
        string = 'FRONT -> '
        for i in range(self.length):
            string += str(self._queue[(self.front+i)%len(self._queue)]) + ' '
        string += '-> BACK'
        return string


# Tests
queue = Queue(4)

print(queue)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print(queue)
queue.dequeue()
queue.dequeue()
queue.enqueue(10)
queue.enqueue(12)
print(queue)