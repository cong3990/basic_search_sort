from read_write_file import input_data, read_input, write_file, check_data
from sort_algorithm import bubble_sort, selection_sort, insertion_sort, merge_sort
from search_algorithm import linear_search, binary_search


def menu():
    """
    Sort Algorithm: Bubble Sort, Selection Sort, Insertion Sort
    Search Algorithm: Linear Search, Binary Search
    """

    # Place-holder to check if data existed when run search or sort function
    a = []
    while True:

        print()
        print("============= WELCOME TO SEARCH AND FIND PROGRAM =============")
        print()
        print("   +--------  MENU --------+")
        print()
        print("   |  1. Manual Input      |")
        print()
        print("   |  2. File Input        |")
        print()
        print("   |  3. Bubble Sort       |")
        print()
        print("   |  4. Selection Sort    |")
        print()
        print("   |  5. Insertion Sort    |")
        print()
        print("   |  6. Linear Search     |")
        print()
        print("   |  7. Binary Search     |")
        print()
        print("   |  0. Exit              |")
        print()
        print("   +-----------------------+")
        print()

        # Ask for what function user wants to execute
        # Make sure input is a number displayed on the menu (0 -> 7)
        while True:
            try:
                func = int(input("Enter the number of the function you would like to implement:\n"))
            except ValueError:
                print("Please select a number displayed on the MENU!")
                continue
            else:
                if func not in range(0, 8):
                    print("Please select a number displayed on the MENU!")
                    continue
                else:
                    break

        # Enter input and store to INPUT.TXT
        if func == 1:
            print("Choice 1: Manual Input")
            enter = input_data()
            if enter == "n":
                continue
            print("Data has been stored in INPUT.TXT.")

        # Get file path and print out elements list
        elif func == 2:
            print("Choice 2: File Input")
            a = read_input()

            # If no output returned, back to menu
            if a == "n":
                continue
            print(f"Input array: '{a}'")

        # Bubble Sort
        elif func == 3:
            print("Choice 3: Bubble Sort")
            # Check if data existed, if not existed, ask for file path and input data
            b = check_data(a)

            # If no output returned, back to menu
            if b == "n":
                continue
            bubble = bubble_sort(b)
            write_file("OUTPUT1.TXT", "w", bubble)
            print("Bubble Sort:", bubble)
            print("Sorted result has been stored in OUTPUT1.TXT")

        # Selection Sort
        elif func == 4:
            print("Choice 4: Selection Sort")
            b = check_data(a)
            if b == "n":
                continue
            select = selection_sort(b)
            write_file("OUTPUT2.TXT", "w", select)
            print("Selection Sort:", select)
            print("Sorted result has been stored in OUTPUT2.TXT")

        # Insertion Sort
        elif func == 5:
            print("Choice 5: Insertion Sort")
            b = check_data(a)
            if b == "n":
                continue
            insert = insertion_sort(b)
            print("Insertion Sort:", insert)
            print("Sorted result has been stored in OUTPUT3.TXT")

        # Linear Search
        elif func == 6:
            print("Choice 6: Linear Search")
            b = check_data(a)
            if b == "n":
                continue

            # Ask for input value that user wants to check
            while True:
                try:
                    x = float(input("Please enter searched input value:\n"))

                # Make sure input value is a number
                except ValueError:
                    print("Input value must be integer. Please input again.")
                    continue
                else:
                    linear = linear_search(b, x)

                    # Length of search result < 1 means list does not have item larger than input value
                    if len(linear) < 1:
                        l_found = "There is no item in list has larger value than input value!"
                    else:
                        l = " ".join(list(map(str, linear)))
                        l_found = "Larger position: " + l
                    break

            write_file("OUTPUT4.TXT", "a", l_found + "\n")
            print(l_found)
            print("Result has been stored in OUTPUT4.TXT")

        # Binary Search
        elif func == 7:
            print("Choice 7: Binary Search")
            b = check_data(a)
            if b == "n":
                continue

            # Sort input list from small to large
            b_sorted = merge_sort(b)
            while True:
                try:
                    x = float(input("Please enter searched input value: \n"))

                # If input value is not a number, input again
                except ValueError:
                    print("Input value must be number. Please input again")
                    continue

                else:
                    binary = binary_search(b_sorted, x)

                    # Return search is -1 means no item match
                    if binary == -1:
                        b_found = "No match item found!"
                    else:
                        b_found = "The righ position: " + str(binary)
                    break
            print(b_found)

        # Exit Program
        elif func == 0:
            print("THANK YOU!!! SEE YOU AGAIN!!!")
            break


if __name__ == "__main__":
    menu()
