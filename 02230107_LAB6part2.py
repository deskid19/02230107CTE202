#Part 2: Merge SortImplementation
#Implementthe merge sort algorithm

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0, 0

    mid = len(arr) // 2
    left, c1, a1 = merge_sort(arr[:mid])
    right, c2, a2 = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    comp = acc = 0

    while i < len(left) and j < len(right):
        comp += 1
        acc += 3   # 2 reads + 1 write

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        acc += 1
        i += 1

    while j < len(right):
        merged.append(right[j])
        acc += 1
        j += 1

    return merged, c1 + c2 + comp, a1 + a2 + acc


# Example
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comp, acc = merge_sort(arr)

print("Original List:", arr)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comp)
print("Number of array accesses:", acc)

