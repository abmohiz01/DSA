'''A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
This means that the last element added to the stack is the first one to be removed.
Think of a stack as a collection of items stacked on top of each other, like a stack of plates.
You can only add or remove items from the top of the stack.'''
class Stack:
    #Constructor
    def __init__(self):
        self.items = []

    '''push function to add items to the stack'''
    def push(self, item):
        self.items.append(item)
    '''Pop function to remove the last element from the stack'''
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Stack:", stack.items)
print("Top item:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack size:", stack.size())
print("Stack:", stack.items)
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
