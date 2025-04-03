# optimized code
if __name__ == '__main__':
    N = int(input())  # Number of commands
    arr = []  # Initialize an empty list

    for _ in range(N):
        command = input().split()  # Read input and split into parts
        operation = command[0]  # Extract command name
        args = list(map(int, command[1:]))  # Convert arguments to integers

        if operation == "print":
            print(arr)  # Special case, as print() is not a list method
        else:
            try:
                getattr(arr, operation)(*args)  # Dynamically execute list method
            except AttributeError:
                print(f"Invalid command: {operation}")
