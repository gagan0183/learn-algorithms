def max_recursion(items):
    if len(items) == 2:
        return items[0] if items[0] > items[1] else items[1]
    sub_max = max_recursion(items[1:])
    return items[0] if items[0] > sub_max else sub_max

print(max_recursion([1, 13, 2, 5, 3]))