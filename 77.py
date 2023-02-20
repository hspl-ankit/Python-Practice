'''Please write a binary search function which searches an item in a sorted list. The function should return the
index of the element to be searched in the list.
'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 3, 5, 7, 9]
x = 5

index = binary_search(arr, x)

if index == -1:
    print("Element not found in list")
else:
    print(f"Element found at index {index}")
