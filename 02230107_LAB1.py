#Task1: Implement the List Class Structure 
class CustomList:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__arr = [None] * self.__capacity

        print(f"Created new CustomList with capacity: {self.__capacity}")
        print(f"Current size: {self.__size}")

# create object
my_list = CustomList()

#Task2: Implement Basic Operations 
class CustomList:
    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__arr = [None] * capacity

        print(f"Created new CustomList with capacity: {self.__capacity}")
        print(f"Current size: {self.__size}")

    # 1. append(element)
    def append(self, element):
        if self.__size < self.__capacity:
            self.__arr[self.__size] = element
            self.__size += 1
            print(f"Appended {element} to the list")
        else:
            print("List is full")

    # 2. get(index)
    def get(self, index):
        if 0 <= index < self.__size:
            print(f"Element at index {index}: {self.__arr[index]}")
            return self.__arr[index]
        else:
            print("Index out of range")

    # 3. set(index, element)
    def set(self, index, element):
        if 0 <= index < self.__size:
            self.__arr[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Index out of range")

    # 4. size()
    def size(self):
        print(f"Current size: {self.__size}")
        return self.__size


# Testing the class
my_list = CustomList()

my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()