#Part 1: Queue Implementation using Array
#Task 1: Implementthe ArrayQueue Class Structure
class ArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity  
        self.front = -1                
        self.rear = -1                  
        self.capacity = capacity

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def display_status(self):
        print(f"Created new Queue with capacity: {self.capacity}")
        print(f"Queue is empty: {self.is_empty()}")


# Test the class
q = ArrayQueue(10)
q.display_status()

#Task 2: Implement Array-based Queue Operations
class ArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = element
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        element = self.queue[self.front]
        self.front += 1

        print(f"Dequeued element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        return self.rear - self.front + 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Display queue:", self.queue[self.front:self.rear + 1])

q = ArrayQueue(10)

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

print("Front element:", q.peek())

q.dequeue()
print("Current queue:", q.queue[q.front:q.rear + 1])

print("Queue size:", q.size())