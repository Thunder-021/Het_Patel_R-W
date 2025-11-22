print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

  
    if not choice.isdigit():
        print("Invalid input! Enter a number from 1 to 3.")
        continue

    choice = int(choice)

  
    if choice == 1:
        rows_input = input("Enter the number of rows for the pattern: ")

        if not rows_input.isdigit():
            print("Invalid! Row count must be a positive number.")
            continue

        rows = int(rows_input)

        if rows <= 0:
            print("Invalid row count. Stopping pattern generation...")
            break  

        print("Pattern:\n")

        for i in range(2, rows + 2):
            print("*" * i)

        pass  

    elif choice == 2:
        start_input = input("Enter the start of the range: ")
        end_input = input("Enter the end of the range: ")

        if not start_input.isdigit() or not end_input.isdigit():
            print("Start and end must be numbers!")
            continue

        start = int(start_input)
        end = int(end_input)

        if start >= end:
            print("Start must be LESS than end. Try again.")
            continue

        total_sum = 0
        print()

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total_sum += num

        print(f"Sum of all numbers from {start} to {end} is: {total_sum}")

   
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
