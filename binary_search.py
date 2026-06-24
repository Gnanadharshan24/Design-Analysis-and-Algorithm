def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  
array = [3, 7, 12, 18, 25, 31, 42]
target = int(input("Enter the element to search: "))
result = binary_search(array, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")