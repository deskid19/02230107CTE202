# Part 1: Sequential Search Implementation
# Implement the Sequential Search Algorithm

# Function definition
def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons   # Target found
    return -1, comparisons       # Target not found

# Sample list and target
arr = [23, 45, 12, 67, 89, 34, 56]
target = 67

# Call the function
index, comparisons = sequential_search(arr, target)

# Display results
print("List:", arr)
print("Searching for", target, "using Sequential Search")

if index != -1:
    print("Found at index", index)
else:
    print("Not found")

print("Number of comparisons:", comparisons)

#Part 2: Binary Search Implementation
#Implementthe Binary Search Algorithm

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1  # Count the comparison below
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons  # Target not found

# Recursive Binary Search
def binary_search_recursive(arr, target, low=0, high=None, comparisons=0):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1, comparisons
    
    mid = (low + high) // 2
    comparisons += 1  # Count the comparison below
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# Example usage:
sorted_list = [12, 23, 34, 45, 56, 67, 89]
target = 67

# Iterative
index_iter, comp_iter = binary_search_iterative(sorted_list, target)
print(f"Iterative: Found at index {index_iter}, Comparisons: {comp_iter}")

# Recursive
index_rec, comp_rec = binary_search_recursive(sorted_list, target)
print(f"Recursive: Found at index {index_rec}, Comparisons: {comp_rec}")