#Part 2: Stack Implementation using Linked List
#Task 3: Implement the Node and LinkedStack Class Structure

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0  
        print("Created new LinkedStack")

    def is_empty(self):
        return self.top is None

# Example usage
stack = LinkedStack()
print("Stack is empty:", stack.is_empty())

#Task 4: Implement Linked List-based Stack Operations
# Node class
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None  
        self._size = 0   
        print("Created new LinkedStack")

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top  
        self.top = new_node       
        self._size += 1
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop element.")
            return None
        popped_element = self.top.data
        self.top = self.top.next 
        self._size -= 1
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            current = self.top
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            print("Current stack:", " -> ".join(map(str, elements)))

# Example usage
stack = LinkedStack()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.peek()
stack.pop()
stack.display()