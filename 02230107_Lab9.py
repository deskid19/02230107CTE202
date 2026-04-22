#Task 1: Implement the Node and List Class Structure
def selection_sort(arr):
    n = len(arr)

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Pass {i+1}: {arr}")

    print("Sorted list:", arr)

arr = [29, 10, 14, 37, 13]

# 🔹 Function call
selection_sort(arr)

#Task 2: Implement Basic Operations
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"Pass {i+1}: {arr}")

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)

arr = [29, 10, 14, 37, 13]

# 🔹 Function call
selection_sort(arr)
       
#Task 3: Create an Index Table for Indexed Search
def create_index_table(arr, block_size):
    index_table = []

    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))

    print("Index table created:")
    for value, index in index_table:
        print(f"{value} -> {index}")

    return index_table

arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

# 🔹 Function call
create_index_table(arr, block_size)

#Task 4: Implement Indexed Search
def indexed_search(arr, index_table, key):
    print("Search key:", key)

    # default range (last block)
    start = index_table[-1][1]
    end = len(arr) - 1

    print("Searching from", start, "to", end)

    for i in range(start, end + 1):
        print("Checking index", i, ":", arr[i])
        if arr[i] == key:
            print(key, "found at index", i)
            return i

    print(key, "not found")
    return -1


# Input
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]

# Key found case
indexed_search(arr, index_table, 45)

#Task 5: Test Indexed Search for a Key Not Found
def indexed_search(arr, index_table, key):
    print("Search key:", key)

    imin = index_table[-1][1]
    imax = len(arr) - 1

    print("Searching range:", imin, "to", imax)

    for i in range(imin, imax + 1):
        print("Checking index", i, ":", arr[i])
        if arr[i] == key:
            print(key, "found at index", i)
            return i

    print(key, "not found")
    return -1


# Input
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]

# Key not in list
indexed_search(arr, index_table, 43)

