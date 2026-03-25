#LAB2
#Task 1: Implementthe Node and List Class Structure
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

ll = LinkedList()

print("Created new LinkedList")
print("Current size:", ll.size)
print("Head:", ll.head)

#Task 2: Implement Basic Operations
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0   

    # 1. append(element)
    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        print(f"Appended {element} to the list")

    # 2. get(index)
    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    # 3. set(index, element)
    def set(self, index, element):
        current = self.head
        for i in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    # 4. size()
    def size(self):
        print("Current size:", self.count)
        return self.count

    # 5. prepend(element)
    def prepend(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1
        print(f"Prepend {element} to the list")

    # display list
    def display(self):
        current = self.head
        print("Print Linked list:", end=" [")
        while current:
            print(current.data, end=" ")
            current = current.next
        print("]")


ll = LinkedList() 
ll.append(5)      
ll.prepend(10)    
ll.prepend(10)  

ll.display() 

