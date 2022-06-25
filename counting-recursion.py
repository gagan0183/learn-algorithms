def counting(items):
    if len(items) == 0:
        return 0
    return 1 + counting(items[1:])

print(counting([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))