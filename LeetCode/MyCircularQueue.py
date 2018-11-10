class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.current = 0
        self.queue = []

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.current < self.size:
            self.queue.append(value)
            self.current += 1

            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.current != 0:
            self.current -= 1
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if len(self.queue) != 0:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.current < self.size:
            return False
        else:
            return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

circularQueue = MyCircularQueue(3)
print(circularQueue.enQueue(1))
print(circularQueue.enQueue(2))
print(circularQueue.enQueue(3))
print(circularQueue.enQueue(4))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.enQueue(4))
print(circularQueue.Rear())
