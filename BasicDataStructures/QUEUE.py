'''Implementation using Collection Module'''
import collections

q = collections.deque()

q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
print("Queue = ",q)
q.pop()
q.pop()
q.pop()
print("Queue = ",q)


'''Implementation Using List'''
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
queue = Queue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")

print("Queue:", queue.items)  # Output: Queue: ['Alice', 'Bob', 'Charlie']
print("Front:", queue.front())  # Output: Front: Alice

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # Output: Dequeued item: Alice
print("Queue size:", queue.size())
print("Queue", queue.items)# Output: Queue size: 2
print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False
