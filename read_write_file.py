def input_data():
    """
    Get input data and write to INPUT.TXT file
    Input n number of integers (n <= 20)
    Input list of integers (using space (" ") or comma (",") to separate items)
    """

    # Check if input n is > 20 or not a number
    get_n = True
    while True:
        try:
            a = float(input("Please enter input number of elements:\nn = "))
            # If n > 20, re-input n
            while float(a) > 20:
                print("n cannot exceed 20. Please input again!")
                a = float(input("Please enter input number of elements:\nn = "))
        # If n is not a number, re-input
        except ValueError:
            print("n must be a number. Please input again!")
            continue
        else:
            break


    while True:
        try:
            b = input("Please enter input elements:\n")
            again = "a"
            # Check if length of input items is <= 20
            while len(b.split()) > 20:
                again = input("Length of input elements cannot exceed 20. Would you like to input again? (Y/N)\n")
                if again[0].lower() == "y":
                    break
                elif again[0].lower() == "n":
                    return "n"
                else:
                    print("Sorry I do not understand. Please enter Yes or No!")
                    continue

            if again[0].lower() == "y":
                continue

            # Remove "," if exist
            if "," in b:
                b = b.replace(",", " ")
            # Check if input has non-digit item
            b = list(map(float, b.split()))

        # If input has non-digit item, re-input
        except ValueError:
            again = input("Elements must be number. Would you like to input again? (Y/N)\n")
            if again[0].lower() == "y":
                continue
            elif again[0].lower() == "n":
                return "n"
            else:
                print("Sorry I do not understand. Please enter Yes or No!")
                continue
        else:
            break

    a = int(a)
    b = " ".join([str(int(x)) for x in b])
    f = open("INPUT.TXT", "w")
    data = f"{a}\n{b}"
    f.write(data)
    f.close()


def read_input():
    """Get data and return a list of integers from INPUT.TXT file"""

    # Open file
    go = True
    while go:
        # Make sure file path is valid
        try:
            f_name = input("Please enter the file path:\n")
            f = open(f_name, "r")
        except FileNotFoundError:
            while True:
                f_not_found = input("File not found. Would you like to enter file path again? (Y/N)\n")
                if f_not_found[0].lower() == "y":
                    break
                elif f_not_found[0].lower() == "n":
                    return "n"
                else:
                    print("Sorry I do not understand. Please enter Yes or No!")
                    continue

        else:
            # get data, splitlines() to remove \n
            data = f.read().splitlines()
            a = data[1]
            f.close()
            break

    return a


def write_file(file_name, mode, data):
    """Write or append (mode "w" or "a") to file_name"""
    f = open(file_name, mode)
    f.write(data)
    f.close()


def check_data(a):
    # If list (a) has been output to program (as a str), assign to b as a list of str
    if len(a) > 0 and a[0].isdigit():
        b = a
    else:
        b = read_input()
        if b == "n":
            return "n"

    # Get list of integers which is at index 1 of data
    # map() to iterate through each item in list and change items into integers
    # return of map is name of map's saved place, so have to cast list
    b = list(map(float, b.split()))

    return b


if __name__ == "__main__":
    from sort_algorithm import *
    from search_algorithm import *

    # 10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3
    input_data()
    lst = read_input()
    not_sort_lst = lst.copy()
    check = sorted(lst)
    bubble = bubble_sort(lst)
    selection = selection_sort(lst)
    insertion = insertion_sort(lst)
    merge = merge_sort(lst)

    print("check", check)
    print("bubble", bubble)
    print("selection", selection)
    print("insertion", insertion)
    print("merge", merge)

    data_bubble = " ".join(list(map(str, bubble)))
    write_file("OUTPUT1.TXT", "w", data_bubble)

    data_selection = " ".join(list(map(str, selection)))
    write_file("OUTPUT2.TXT", "w", data_selection)

    data_insertion = " ".join(list(map(str, insertion)))
    write_file("OUTPUT3.TXT", "w", data_insertion)

    x = 5
    linear = linear_search(not_sort_lst, x)
    binary = binary_search(merge, x)
    if len(linear) < 1:
        linear_found = "Not Found!"
    else:
        linear_found = " ".join(list(map(str, linear)))

    if not binary:
        binary_found = "Not Found!"
    else:
        binary_found = str(binary)

    print(linear_found)
    print(binary_found)

    write_file("OUTPUT4.TXT", "a", linear_found + "\n")
