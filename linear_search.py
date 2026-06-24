arr = [12, 45, 7, 23, 56, 89, 34]
target = int(input("Enter the element to search: "))
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at index {i}")
        found = True
        break

# Step 4: If not found
if not found:
    print("Element not found in the array")