def find_smallest(items):
    smallest = items[0]
    for i in range(1, len(items)):
        if items[i] < smallest:
            smallest = items[i]
    return smallest

def selection_sort(items):
    sorted_items = []
    for i in range(len(items)):
        smallest = find_smallest(items)
        sorted_items.append(smallest)
        items.remove(smallest)
    return sorted_items

print(selection_sort([10, 1, 3, 9, 30, 20]))