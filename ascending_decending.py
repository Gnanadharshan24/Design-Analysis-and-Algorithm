n = int(input("Enter the size of the array: "))
arr = []

print("Enter the array elements:")
for i in range(n):
    arr.append(int(input()))
while True:
    print("\n----- MENU -----")
    print("1. Sort in Ascending Order")
    print("2. Sort in Descending Order")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arr.sort()
        print("Ascending Order:", arr)

    elif choice == 2:
        arr.sort(reverse=True)
        print("Descending Order:", arr)

    else:
        print("Invalid Choice! Please try again.")