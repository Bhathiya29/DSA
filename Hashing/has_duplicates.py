def has_duplicates(arr):
    original = set()

    for element in arr:
        if element in original:
            return True
        original.add(element)

    return False

# Example
arr = [1, 2, 3, 4, 5, 6, 1]
print(has_duplicates(arr))  