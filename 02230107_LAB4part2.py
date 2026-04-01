#Part 2: Queue implementation using Linked List
#Task 3: Implementthe Node and LinkedStack Class Structure 
# Node class
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None     

class LinkedQueue:
    def __init__(self):
        self.front = None    
        self.rear = None     
        self.size_count = 0   
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.front is None

    def display_status(self):
        print("Queue is empty:", self.is_empty())

q = LinkedQueue()
q.display_status()

#Task 4: Implement Linked List-based Queue Operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_count = 0
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size_count += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        removed = self.front.data
        self.front = self.front.next

        if self.front is None: 
            self.rear = None

        self.size_count -= 1
        print(f"Dequeued element: {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def size(self):
        return self.size_count

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print("Display queue:[" + ",".join(elements) + "]")

    def display_linked(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        result = ""

        while current:
            result += str(current.data) + " -> "
            current = current.next

        result += "null"
        print("Current queue:", result)

q = LinkedQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

print("Front element:", q.peek())

q.dequeue()
q.display_linked()

print("Queue size:", q.size())