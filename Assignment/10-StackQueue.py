class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)


# Example usage of Stack
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack after pop:", stack.items)
print("Size of Stack:", stack.size())

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Queue is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)


# Example usage of Queue
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.items)
print("Size of Queue:", queue.size())
