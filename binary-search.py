def binary_search(sorted_array, search_item):
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]
        if guess == search_item:
            return mid
        if search_item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search([1, 3, 5, 9, 11, 13, 15], 13))
