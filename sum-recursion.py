def sum_recursion(list):
    if len(list) == 0:
        return 0
    return list[0] + sum_recursion(list[1:])

print(sum_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))