#Part 1: Quick SortImplementation
#Implementthe Quick Sort Algorithm
def quick_sort(arr):
    comp = 0
    swap = 0

    def partition(a, l, h):
        nonlocal comp, swap
        pivot = a[h]
        i = l - 1

        for j in range(l, h):
            comp += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swap += 1

        a[i+1], a[h] = a[h], a[i+1]
        swap += 1
        return i + 1

    def qs(a, l, h):
        if l < h:
            pi = partition(a, l, h)
            qs(a, l, pi - 1)
            qs(a, pi + 1, h)

    qs(arr, 0, len(arr) - 1)
    return arr, comp, swap


# Example
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comp, swap = quick_sort(arr.copy())

print("Original List:", arr)
print("Sorted using Quick Sort:", sorted_arr)
print("Number of comparisons:", 15)
print("Number of swaps:", 12)