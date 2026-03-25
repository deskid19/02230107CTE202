#Part 1: Stack Implementation using Array
#Task 1: Implementthe ArrayStack Class Structure

class ArrayStack:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._stack = [None] * capacity
        # Variable to track the top of the stack
        self._top = -1
        # Store capacity
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")

    def is_empty(self):
        # Returns True if stack is empty
        return self._top == -1

# Example usage
stack = ArrayStack()        # Creates a stack with default capacity 10
print("Stack is empty:", stack.is_empty())

#Task 2: Implement Array-based Stack Operations
class ArrayStack:
    def __init__(self, capacity=10):
        self._stack = [None] * capacity
        self._top = -1
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")

    def push(self, element):
        if self._top + 1 >= self._capacity:
            print("Stack overflow! Cannot push element.")
            return
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop element.")
            return None
        popped_element = self._stack[self._top]
        self._stack[self._top] = None 
        self._top -= 1
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]

    def is_empty(self):
        return self._top == -1

    def size(self):
        return self._top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Display stack:", self._stack[:self._top + 1])

# Example usage
stack = ArrayStack()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.peek()
stack.pop()
print("Stack size:", stack.size())
stack.display()