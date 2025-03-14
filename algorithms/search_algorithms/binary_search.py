def binary_serch_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1

def binary_search_recursive(arr, target):
    def binary_search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    left, right = 0, len(arr) - 1
    return binary_search(left, right)
