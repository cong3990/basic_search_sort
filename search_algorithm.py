def linear_search(a, x):
    """Search through each item of the list to find match item"""

    larger = []

    for i in range(len(a)):
        # Return item's index in list if match item is found
        if a[i] > x:
            larger.append(i)

    return larger



def binary_search(lst, x):
    """Search for first match of a value x in a sorted list and return its index in list using binary search"""

    # Setup for first loop
    lower_bound = 0
    upper_bound = len(lst) - 1

    # Place-holder for found value
    hold = -1

    # Divide list to smaller lists until there is no more item to search
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        # Find the halves that may contain x
        if lst[mid] > x:
            upper_bound = mid - 1

        elif lst[mid] < x:
            lower_bound = mid + 1

        # if match item is found, hold its index, keep checking the left side of found item
        # so at the end of the loop, the most left matched (first matched) item will be hold and return
        else:
            hold = mid
            upper_bound = mid - 1

    return hold


if __name__ == "__main__":
    lst = [10, 12, 2, 39, 18, 12, 1, 24, 13, 14, 12, 3]

    x = 3
    lin = linear_search(lst, x)
    print("linear search larger:", lin)

    s_lst = sorted([float(i) for i in lst.copy()])
    y = 3
    print("sorted list:", s_lst)
    binary = binary_search(s_lst, y)
    print("binary search:", binary)
