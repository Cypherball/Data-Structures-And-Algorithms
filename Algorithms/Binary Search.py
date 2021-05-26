def binary_search(data, element):
    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if data[mid] == element:
            return mid
        elif data[mid] < element:
            low = mid + 1
        else: high = mid - 1
    
    return -1


def binary_search_recursive(data, element, low = 0, high = None):
    if high == None: high = len(data) - 1
    if low <= high:
        mid = (high + low) // 2
        if data[mid] == element:
            return mid
        elif data[mid] < element:
            return binary_search_recursive(data, element, mid + 1, high)
        else:
            return binary_search_recursive(data, element, low, mid - 1)
    else: return -1

data = [2, 5, 9, 10, 12, 22, 25, 29, 32, 55, 99, 205]

print('-----Iterative-----')
print(binary_search(data, 5))
print(binary_search(data, 22))
print(binary_search(data, 102))

print('\n-----Recursive-----')
print(binary_search_recursive(data, 5))
print(binary_search_recursive(data, 22))
print(binary_search_recursive(data, 102))
